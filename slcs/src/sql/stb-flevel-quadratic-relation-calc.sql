-- set DATE_SUB_2=20220823;
-- set DATE_SUB_2=20220821;
-- set DATE_SUB_1=20230202;
set hivevar:vuid_threshold=8*10000;
set hivevar:vuid_threshold=1000;
set hivevar:fanscnt_ratio_threshold=0.3;
-- val df = spark.read.option("header", true).option("delimiter", "\t").csv("file:///data0/users/suanec/suanec-stb-2023011219.tsv");def f(_str : String, _strs: String*) = df.select(_str, _strs:_*).show(false);df.registerTempTable("t");
-- select split(ff1001, '|') from wbml_src.src_sample_waic_sample_super_topic_top_page_base_sample where dt = 20230201 and hour = 05 limit 3
with st_bottom_base_sample_raw as (
  select *
  from wbml_src.src_sample_waic_sample_super_topic_top_page_base_sample
  where dt = ${DATE_SUB_1}
  -- where dt = 20230201
  -- and hour = 05
  -- limit 30000
)
, st_bottom_base_sample as (
  select distinct uid, 
  last_value(ff1001) over(partition by uid order by length(ff1001)) as ff1001, 
  last_value(sf1101) over(partition by uid order by length(sf1101))  as sf1101
  from st_bottom_base_sample_raw
)
, stid_filterd as (
  select distinct stid
  from st_bottom_base_sample_raw
  where ost115 is not null
  and instr(ost115, '娱乐') <= 0
  and instr(ost115, '明星') <= 0
  and instr(ost115, 'CP') <= 0
)
, all_user_vuid_table as (
  -- select distinct wm1082 
  -- from om115_filterd_sample
  select uid, vuid 
  from st_bottom_base_sample
  -- lateral view explode(split(ff1001, '\\\\|')) view_table_name as vuid
  lateral view explode(split(ff1001, '\\|')) view_table_name as vuid
)
-- select uid, vuid from all_user_vuid_table;
, all_user_stid_table as (
  -- select distinct wm1082 
  -- from om115_filterd_sample
  select uid, follow_stid 
  from st_bottom_base_sample
  -- lateral view explode(split(ff1001, '\\\\|')) view_table_name as follow_stid
  lateral view explode(split(sf1101, '\\|')) view_table_name as follow_stid
)
, user_stid_table as (
  select * 
  from all_user_stid_table
  left semi join stid_filterd
  on stid_filterd.stid = all_user_stid_table.follow_stid
)
-- select * from user_stid_table;
, vuid_table as (
  select * from (
    select vuid, count(uid) as fans_count
    from all_user_vuid_table
    group by vuid 
  ) vuid_fans_count_temp_t
  -- where fans_count > 8 * 10000
  where fans_count > ${hivevar:vuid_threshold}
)
, vuid_fans_table as (
  select uid, all_user_vuid_table.vuid
  from all_user_vuid_table
  left semi join vuid_table
  on all_user_vuid_table.vuid = vuid_table.vuid
)
-- select vuid from vuid_table;
-- select * from user_stid_table left join vuid_fans_table on vuid_fans_table.uid = user_stid_table.uid limit 30;
-- select * from vuid_fans_table left join user_stid_table on vuid_fans_table.uid = user_stid_table.uid limit 30;
-- select vuid_fans_table.uid, vuid, follow_stid from user_stid_table left join vuid_fans_table on vuid_fans_table.uid = user_stid_table.uid limit 30;
-- , vuid_fans_stid_table_0 as (
--   select vuid_fans_table.uid, vuid_fans_table.vuid, user_stid_table.follow_stid
--   from vuid_fans_table
--   left join user_stid_table
--   on all_user_vuid_table.uid = user_stid_table.uid
-- )
, vuid_fans_stid_table as (
  select all_user_vuid_table.uid, all_user_vuid_table.vuid, vuid_table.fans_count, user_stid_table.follow_stid
  from vuid_table
  left join all_user_vuid_table
  on all_user_vuid_table.vuid = vuid_table.vuid
  left join 
  on all_user_vuid_table.uid = user_stid_table.uid
  where follow_stid is not null
)
-- select * from vuid_fans_stid_table;
-- select * from user_stid_table left join vuid_fans_table on vuid_fans_table.uid = user_stid_table.uid limit 30;
, vuid_stid_fanscnt_table as (
  select vuid, follow_stid as stid, count(uid) as fans_count_in_stid, fans_count
  from vuid_fans_stid_table
  group by vuid, follow_stid, fans_count
)
, vuid_stid_fanscnt_percent_table as (
  select vuid, stid, fans_count_in_stid, fans_count
  from vuid_stid_fanscnt_table
  left semi join stid_filterd
  on stid_filterd.stid = vuid_stid_fanscnt_table.stid
  where fans_count_in_stid < fans_count and
  fans_count_in_stid * 1.0 / fans_count > ${hivevar:fanscnt_ratio_threshold}
)

-- select * from vuid_stid_fanscnt_percent_table order by fans_count_in_stid limit 30;

-- select count(wm1082) from vuid;


-- ff1001 用户关注的uid列表
-- sf1101  用户关注超话
-- wm1082 微博作者uid
-- om115  发博者flevel

-- dt=20230130
-- +--------+-----------+-------+
-- | om115  | count(1)  | hour  |
-- +--------+-----------+-------+
-- | 4      | 161026    | 04    |
-- | -1     | 760573    | 04    |
-- | 1      | 86045     | 04    |
-- | 6      | 272971    | 04    |
-- | 2      | 46148     | 04    |
-- | 5      | 287158    | 04    |
-- | 3      | 163271    | 04    |
-- | -1     | 496505    | 05    |
-- | 6      | 191912    | 05    |
-- | 5      | 179895    | 05    |
-- | 2      | 38643     | 05    |
-- | 3      | 114177    | 05    |
-- | 4      | 95188     | 05    |
-- | 1      | 66933     | 05    |
-- +--------+-----------+-------+

, vuid_fans_atten_stid_count as (
  select
    json2material('',
        '',
        '50287',
        stid,
        'upd',
        concat_ws('@', vuid, cast(fans_count_in_stid as String)),
        '',
        concat_ws("||", concat_ws('::', 'fans_count', cast(fans_count_in_stid as String)))
        -- ""
        -- concat_ws("||", concat_ws('::', 'category', rst_category), concat_ws('::', 'ori_score', rst_score))
        
    ) as material_json
    from vuid_stid_fanscnt_percent_table
)
-- select * from vuid_fans_atten_stid_count limit 10;
select count(1) from vuid_fans_atten_stid_count limit 10;
