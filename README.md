# FLiP-Py-Pi-GasThermal

Apache Pulsar, Python, Raspberry Pi, Gas Sensor + Thermal Camera Sensors, Apache Flink, Trino/Presto SQL

![ThermalCam](https://github.com/tspannhw/FLiP-Py-Pi-GasThermal/blob/main/mlx90640-2022-03-04-15-36-31.gif)

## Sensors

* Pimoroni BreakoutGarden:  SGP30 
  - Sensiron SGP30 TVOC and eCO2 sensor (datasheet)
  - TVOC sensing from 0-60,000 ppb (parts per billion)
  - CO2 sensing from 400 to 60,000 ppm (parts per million)
* Pimoroni BreakoutGarden: MLX90640 Thermal Camera

![HardWare](https://github.com/tspannhw/FLiP-Py-Pi-GasThermal/blob/main/garden3.jpeg?raw=true)

### Architecture

![designthis](https://github.com/tspannhw/FLiP-Py-Pi-GasThermal/blob/main/airqualityedge.png?raw=true)
![more](https://github.com/tspannhw/FLiP-Py-Pi-GasThermal/blob/main/airqualityexample-2022-02-02-0846.png?raw=true)


### Build

````
bin/pulsar-admin topics create persistent://public/default/garden3

bin/pulsar-client consume "persistent://public/default/garden3" -s "garden3reader" -n 0

class Garden(Record):
    cpu = Float()
    diskusage = String()
    endtime = String()
    equivalentco2ppm = String()
    host = String()
    hostname = String()
    ipaddress = String()
    macaddress = String()
    memory = Float()
    rowid = String()
    runtime = Integer()
    starttime = String()
    systemtime = String()
    totalvocppb = String()
    ts = Integer()
    uuid = String()

----- got message -----
key:[garden3_uuid_yvs_20220306191528], properties:[], content:{
 "cpu": 0.0,
 "diskusage": "103496.6 MB",
 "endtime": "1646594128.2460103",
 "equivalentco2ppm": "  413",
 "host": "garden3",
 "hostname": "garden3",
 "ipaddress": "192.168.1.198",
 "macaddress": "dc:a6:32:32:98:20",
 "memory": 9.2,
 "rowid": "20220306191528_707b34d4-7299-4233-a495-d2d97393e834",
 "runtime": 0,
 "starttime": "03/06/2022 14:15:28",
 "systemtime": "03/06/2022 14:15:29",
 "totalvocppb": "    5",
 "ts": 1646594129,
 "uuid": "garden3_uuid_yvs_20220306191528"
}

presto> select * from pulsar."public/default"."garden3";
 cpu |  diskusage  |      endtime       | equivalentco2ppm |  host   | hostname |   ipaddress   |    macaddress     | memory |                        rowid                        | runtime |      
-----+-------------+--------------------+------------------+---------+----------+---------------+-------------------+--------+-----------------------------------------------------+---------+------
 6.5 | 103496.5 MB | 1646594650.7116666 |   418            | garden3 | garden3  | 192.168.1.198 | dc:a6:32:32:98:20 |    9.2 | 20220306192410_197b6b0c-b86c-4191-9e9c-11777767825e |       0 | 03/06
 6.7 | 103496.5 MB | 1646594651.7441382 |   418            | garden3 | garden3  | 192.168.1.198 | dc:a6:32:32:98:20 |    9.2 | 20220306192411_4dab3212-423b-46a9-ae39-b10eb363336d |       0 | 03/06
 1.3 | 103496.5 MB | 1646594652.7764313 |   421            | garden3 | garden3  | 192.168.1.198 | dc:a6:32:32:98:20 |    9.2 | 20220306192412_d24a819b-4ca1-489a-9683-da48bc37185c |       0 | 03/06
 0.2 | 103496.5 MB | 1646594653.810233  |   421            | garden3 | garden3  | 192.168.1.198 | dc:a6:32:32:98:20 |    9.2 | 20220306192413_f4e43177-2486-4a36-b27a-903028d6aacf |       0 | 03/06
 0.0 | 103496.5 MB | 1646594654.8467774 |   416            | garden3 | garden3  | 192.168.1.198 | dc:a6:32:32:98:20 |    9.2 | 20220306192414_558d3db8-725a-46ec-ad1f-89f8067142f8 |       0 | 03/06
 0.0 | 103496.5 MB | 1646594655.880628  |   420            | garden3 | garden3  | 192.168.1.198 | dc:a6:32:32:98:20 |    9.2 | 20220306192415_1eeea533-7f7e-4945-a089-d4b2f8681e14 |       0 | 03/06
 0.0 | 103496.5 MB | 1646594656.9145741 |   418            | garden3 | garden3  | 192.168.1.198 | dc:a6:32:32:98:20 |    9.2 | 20220306192416_d7d8c6ea-2adf-4704-8f49-3108a7328f26 |       0 | 03/06
 0.0 | 103496.5 MB | 1646594657.9489982 |   425            | garden3 | garden3  | 192.168.1.198 | dc:a6:32:32:98:20 |    9.2 | 20220306192417_c71cbb6e-c59f-4855-84ae-b796fd3d7a76 |       0 | 03/06
 0.0 | 103496.5 MB | 1646594658.9828157 |   420            | garden3 | garden3  | 192.168.1.198 | dc:a6:32:32:98:20 |    9.2 | 20220306192418_c14204dd-4c1c-4e76-a272-8ddecd11a97c |       0 | 03/06
 0.0 | 103496.5 MB | 1646594660.0187812 |   420            | garden3 | garden3  | 192.168.1.198 | dc:a6:32:32:98:20 |    9.2 | 20220306192419_c7583063-06e0-4601-806a-96619b6bb136 |       0 | 03/06
 0.0 | 103496.5 MB | 1646594661.0531507 |   428            | garden3 | garden3  | 192.168.1.198 | dc:a6:32:32:98:20 |    9.2 | 20220306192421_57e4a8ed-af6f-4dd0-b143-f29f1a211fdb |       0 | 03/06
 0.0 | 103496.5 MB | 1646594662.087301  |   421            | garden3 | garden3  | 192.168.1.198 | dc:a6:32:32:98:20 |    9.2 | 20220306192422_cf2ce36e-c996-41ac-baec-db292cffdd37 |       0 | 03/06
 6.2 | 103496.5 MB | 1646594663.1214898 |   415            | garden3 | garden3  | 192.168.1.198 | dc:a6:32:32:98:20 |    9.2 | 20220306192423_30b13428-ac2e-4929-b9f5-c4c3fbc3312a |       0 | 03/06
 6.5 | 103496.5 MB | 1646594664.1541135 |   424            | garden3 | garden3  | 192.168.1.198 | dc:a6:32:32:98:20 |    9.2 | 20220306192424_d1517315-85fa-4923-b634-9b673c5b20ba |       0 | 03/06
 3.6 | 103496.5 MB | 1646594665.1890867 |   417            | garden3 | garden3  | 192.168.1.198 | dc:a6:32:32:98:20 |    9.2 | 20220306192425_3984b0bc-a92e-4458-834c-e65259bb7a4d |       0 | 03/06
 0.0 | 103496.5 MB | 1646594666.221572  |   422            | garden3 | garden3  | 192.168.1.198 | dc:a6:32:32:98:20 |    9.2 | 20220306192426_e0debd83-47e8-43f7-8ec5-cf0dbc27b87e |       0 | 03/06
 0.0 | 103496.5 MB | 1646594667.2555919 |   424            | garden3 | garden3  | 192.168.1.198 | dc:a6:32:32:98:20 |    9.2 | 20220306192427_6ec920e7-56d2-4730-bddc-e18592cf1210 |       0 | 03/06
 0.0 | 103496.5 MB | 1646594668.2893167 |   428            | garden3 | garden3  | 192.168.1.198 | dc:a6:32:32:98:20 |    9.2 | 20220306192428_434b4458-6f89-4161-b967-f29796d8bf5d |       0 | 03/06
 0.0 | 103496.5 MB | 1646594669.3234618 |   426            | garden3 | garden3  | 192.168.1.198 | dc:a6:32:32:98:20 |    9.2 | 20220306192429_5bb29c2e-d078-405d-b8f6-967ea4753b3f |       0 | 03/06
 0.0 | 103496.5 MB | 1646594670.359024  |   421            | garden3 | garden3  | 192.168.1.198 | dc:a6:32:32:98:20 |    9.2 | 20220306192430_05b86f6b-4d28-497c-acd6-d14f7ce27157 |       0 | 03/06
 0.0 | 103496.5 MB | 1646594671.392967  |   432            | garden3 | garden3  | 192.168.1.198 | dc:a6:32:32:98:20 |    9.2 | 20220306192431_b7a2955a-6f39-4439-8eb9-27d7a2633836 |       0 | 03/06
 0.0 | 103496.5 MB | 1646594672.4271743 |   426            | garden3 | garden3  | 192.168.1.198 | dc:a6:32:32:98:20 |    9.2 | 20220306192432_29861384-fc30-4deb-bc1d-b7f2d27ef89d |       0 | 03/06
 0.0 | 103496.5 MB | 1646594673.4611707 |   424            | garden3 | garden3  | 192.168.1.198 | dc:a6:32:32:98:20 |    9.2 | 20220306192433_25435335-39fe-4294-b913-95c63537a743 |       0 | 03/06
 0.0 | 103496.5 MB | 1646594674.4951062 |   424            | garden3 | garden3  | 192.168.1.198 | dc:a6:32:32:98:20 |    9.2 | 20220306192434_a52a90e8-b11c-467b-b87f-936432bc8988 |       0 | 03/06
 3.3 | 103496.5 MB | 1646594675.531778  |   436            | garden3 | garden3  | 192.168.1.198 | dc:a6:32:32:98:20 |    9.2 | 20220306192435_48bab6a9-9f2e-443b-9fed-f096f6c24ebd |       0 | 03/06
 6.5 | 103496.5 MB | 1646594676.5642908 |   433            | garden3 | garden3  | 192.168.1.198 | dc:a6:32:32:98:20 |    9.2 | 20220306192436_761f79dc-06f6-4ed3-8062-5227b6842b77 |       0 | 03/06
 6.2 | 103496.5 MB | 1646594677.5965276 |   421            | garden3 | garden3  | 192.168.1.198 | dc:a6:32:32:98:20 |    9.2 | 20220306192437_6d8d49c9-0519-4825-b6b7-ed435e9fe747 |       0 | 03/06
 0.0 | 103496.5 MB | 1646594678.6290672 |   423            | garden3 | garden3  | 192.168.1.198 | dc:a6:32:32:98:20 |    9.2 | 20220306192438_a920872d-f152-4b18-94a7-b4dfe5641482 |       0 | 03/06
 0.0 | 103496.5 MB | 1646594679.6629703 |   418            | garden3 | garden3  | 192.168.1.198 | dc:a6:32:32:98:20 |    9.2 | 20220306192439_032ce574-10f6-4b50-b5e8-102b466af65a |       0 | 03/06
 0.0 | 103496.5 MB | 1646594680.699419  |   420            | garden3 | garden3  | 192.168.1.198 | dc:a6:32:32:98:20 |    9.2 | 20220306192440_cde6f78a-d028-4f87-a95b-156bac0ee0c2 |       0 | 03/06
 0.0 | 103496.5 MB | 1646594681.7338123 |   424            | garden3 | garden3  | 192.168.1.198 | dc:a6:32:32:98:20 |    9.2 | 20220306192441_7400689a-6974-4ff2-a688-96c317d45d03 |       0 | 03/06
 0.0 | 103496.5 MB | 1646594682.767776  |   417            | garden3 | garden3  | 192.168.1.198 | dc:a6:32:32:98:20 |    9.2 | 20220306192442_46696fa7-295c-4fe6-bf49-8d8405e21cf5 |       0 | 03/06
 0.0 | 103496.5 MB | 1646594683.8017883 |   420            | garden3 | garden3  | 192.168.1.198 | dc:a6:32:32:98:20 |    9.2 | 20220306192443_4de9f79c-0169-49d6-b337-fb57dcb5cf7e |       0 | 03/06
 0.0 | 103496.5 MB | 1646594684.8360054 |   422            | garden3 | garden3  | 192.168.1.198 | dc:a6:32:32:98:20 |    9.2 | 20220306192444_63081ac4-2c87-462d-bc16-ab506e9c6db2 |       0 | 03/06
 0.0 | 103496.5 MB | 1646594685.8720167 |   420            | garden3 | garden3  | 192.168.1.198 | dc:a6:32:32:98:20 |    9.2 | 20220306192445_fee13e36-26c6-4f06-894c-8b96cb0f3bae |       0 | 03/06
 0.0 | 103496.5 MB | 1646594686.90594   |   431            | garden3 | garden3  | 192.168.1.198 | dc:a6:32:32:98:20 |    9.2 | 20220306192446_8aaa423d-bfe3-43e8-8653-d554c2afb8d6 |       0 | 03/06
 0.8 | 103496.4 MB | 1646594687.939747  |   416            | garden3 | garden3  | 192.168.1.198 | dc:a6:32:32:98:20 |    9.2 | 20220306192447_bfe339cd-3fb4-4d2a-b612-3a2363e1b83b |       0 | 03/06
 6.5 | 103496.4 MB | 1646594688.9728699 |   424            | garden3 | garden3  | 192.168.1.198 | dc:a6:32:32:98:20 |    9.2 | 20220306192448_8809fc3e-75f8-4aca-a141-6e5d4872b0de |       0 | 03/06
 6.5 | 103496.4 MB | 1646594690.0051649 |   412            | garden3 | garden3  | 192.168.1.198 | dc:a6:32:32:98:20 |    9.2 | 20220306192449_0d0b4b62-0321-4bcd-952b-14607333d9f5 |       0 | 03/06

presto> desc pulsar."public/default"."garden3";
      Column       |   Type    | Extra |                                   Comment                                   
-------------------+-----------+-------+-----------------------------------------------------------------------------
 cpu               | real      |       | ["null","float"]                                                            
 diskusage         | varchar   |       | ["null","string"]                                                           
 endtime           | varchar   |       | ["null","string"]                                                           
 equivalentco2ppm  | varchar   |       | ["null","string"]                                                           
 host              | varchar   |       | ["null","string"]                                                           
 hostname          | varchar   |       | ["null","string"]                                                           
 ipaddress         | varchar   |       | ["null","string"]                                                           
 macaddress        | varchar   |       | ["null","string"]                                                           
 memory            | real      |       | ["null","float"]                                                            
 rowid             | varchar   |       | ["null","string"]                                                           
 runtime           | integer   |       | ["null","int"]                                                              
 starttime         | varchar   |       | ["null","string"]                                                           
 systemtime        | varchar   |       | ["null","string"]                                                           
 totalvocppb       | varchar   |       | ["null","string"]                                                           
 ts                | integer   |       | ["null","int"]                                                              
 uuid              | varchar   |       | ["null","string"]                                                           
 __partition__     | integer   |       | The partition number which the message belongs to                           
 __event_time__    | timestamp |       | Application defined timestamp in milliseconds of when the event occurred    
 __publish_time__  | timestamp |       | The timestamp in milliseconds of when event as published                    
 __message_id__    | varchar   |       | The message ID of the message used to generate this row                     
 __sequence_id__   | bigint    |       | The sequence ID of the message used to generate this row                    
 __producer_name__ | varchar   |       | The name of the producer that publish the message used to generate this row 
 __key__           | varchar   |       | The partition key for the topic                                             
 __properties__    | varchar   |       | User defined properties    
 
````

Presto/Trino gives us access to all that tasty meta data for each message/event/row/record/thing/data stuff.   All with special names to help prevent collisions.

#### Meta Data

* __partition__  - if we have a partitioned topic, which partition does this message belong to.
* __event_time__ - you know what time it is!   Timestamp in ms for event action.
* __publish_time__ - when was this message published to the topic?
* __message_id__ - unique id for this message
* __sequence_id__ - ordering information for this message
* __producer_name__ - who sent me this?
* __key__ - did you assign a key like I asked you to?
* __properties__ - all those extra fields you added around the payload



### Spark Structured Streaming

* https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html#output-sinks

````
val dfPulsar = spark.readStream.format("pulsar").option("service.url", "pulsar://localhost:6650").option("admin.url", "http://localhost:8080").option("topic", "persistent://public/default/garden3").load()
dfPulsar.printSchema()
val pQuery = dfPulsar.selectExpr("*").writeStream.format("parquet").option("truncate", false) .option("checkpointLocation", "/tmp/checkpoint").option("path", "/opt/demo/gasthermal").start()
    
pQuery.explain()
pQuery.awaitTermination()
pQuery.stop()

// can be "orc", "json", "csv", etc.

````

![Spark](https://github.com/tspannhw/FLiP-Py-Pi-GasThermal/blob/main/airqualitysparkschema.jpg?raw=true)


### Show Me The Data

We can visualize data from Apache Pulsar by consuming it through the web sockets interface in a simple JQuery Single Page Web Application like below.

![JavaScript](https://github.com/tspannhw/FLiP-Py-Pi-GasThermal/blob/main/airqualitytable.jpg?raw=true)


### Example Parquet Files

````
pip3 install parquet-tools -U

parquet-tools inspect part-00000-b7e1f8dc-956d-4130-bc59-7b1435e41391-c000.snappy.parquet

############ file meta data ############
created_by: parquet-mr version 1.12.1 (build 2a5c06c58fa987f85aa22170be14d927d5ff6e7d)
num_columns: 23
num_rows: 1
num_row_groups: 1
format_version: 1.0
serialized_size: 5071


############ Columns ############
cpu
diskusage
endtime
equivalentco2ppm
host
hostname
ipaddress
macaddress
memory
rowid
runtime
starttime
systemtime
totalvocppb
ts
uuid
__key
__topic
__messageId
__publishTime
__eventTime
key
value

############ Column(cpu) ############
name: cpu
path: cpu
max_definition_level: 1
max_repetition_level: 0
physical_type: FLOAT
logical_type: None
converted_type (legacy): NONE

############ Column(diskusage) ############
name: diskusage
path: diskusage
max_definition_level: 1
max_repetition_level: 0
physical_type: BYTE_ARRAY
logical_type: String
converted_type (legacy): UTF8

############ Column(endtime) ############
name: endtime
path: endtime
max_definition_level: 1
max_repetition_level: 0
physical_type: BYTE_ARRAY
logical_type: String
converted_type (legacy): UTF8

############ Column(equivalentco2ppm) ############
name: equivalentco2ppm
path: equivalentco2ppm
max_definition_level: 1
max_repetition_level: 0
physical_type: BYTE_ARRAY
logical_type: String
converted_type (legacy): UTF8

############ Column(host) ############
name: host
path: host
max_definition_level: 1
max_repetition_level: 0
physical_type: BYTE_ARRAY
logical_type: String
converted_type (legacy): UTF8

############ Column(hostname) ############
name: hostname
path: hostname
max_definition_level: 1
max_repetition_level: 0
physical_type: BYTE_ARRAY
logical_type: String
converted_type (legacy): UTF8

############ Column(ipaddress) ############
name: ipaddress
path: ipaddress
max_definition_level: 1
max_repetition_level: 0
physical_type: BYTE_ARRAY
logical_type: String
converted_type (legacy): UTF8

############ Column(macaddress) ############
name: macaddress
path: macaddress
max_definition_level: 1
max_repetition_level: 0
physical_type: BYTE_ARRAY
logical_type: String
converted_type (legacy): UTF8

############ Column(memory) ############
name: memory
path: memory
max_definition_level: 1
max_repetition_level: 0
physical_type: FLOAT
logical_type: None
converted_type (legacy): NONE

############ Column(rowid) ############
name: rowid
path: rowid
max_definition_level: 1
max_repetition_level: 0
physical_type: BYTE_ARRAY
logical_type: String
converted_type (legacy): UTF8

############ Column(runtime) ############
name: runtime
path: runtime
max_definition_level: 1
max_repetition_level: 0
physical_type: INT32
logical_type: None
converted_type (legacy): NONE

############ Column(starttime) ############
name: starttime
path: starttime
max_definition_level: 1
max_repetition_level: 0
physical_type: BYTE_ARRAY
logical_type: String
converted_type (legacy): UTF8

############ Column(systemtime) ############
name: systemtime
path: systemtime
max_definition_level: 1
max_repetition_level: 0
physical_type: BYTE_ARRAY
logical_type: String
converted_type (legacy): UTF8

############ Column(totalvocppb) ############
name: totalvocppb
path: totalvocppb
max_definition_level: 1
max_repetition_level: 0
physical_type: BYTE_ARRAY
logical_type: String
converted_type (legacy): UTF8

############ Column(ts) ############
name: ts
path: ts
max_definition_level: 1
max_repetition_level: 0
physical_type: INT32
logical_type: None
converted_type (legacy): NONE

############ Column(uuid) ############
name: uuid
path: uuid
max_definition_level: 1
max_repetition_level: 0
physical_type: BYTE_ARRAY
logical_type: String
converted_type (legacy): UTF8

############ Column(__key) ############
name: __key
path: __key
max_definition_level: 1
max_repetition_level: 0
physical_type: BYTE_ARRAY
logical_type: None
converted_type (legacy): NONE

############ Column(__topic) ############
name: __topic
path: __topic
max_definition_level: 1
max_repetition_level: 0
physical_type: BYTE_ARRAY
logical_type: String
converted_type (legacy): UTF8

############ Column(__messageId) ############
name: __messageId
path: __messageId
max_definition_level: 1
max_repetition_level: 0
physical_type: BYTE_ARRAY
logical_type: None
converted_type (legacy): NONE

############ Column(__publishTime) ############
name: __publishTime
path: __publishTime
max_definition_level: 1
max_repetition_level: 0
physical_type: INT96
logical_type: None
converted_type (legacy): NONE

############ Column(__eventTime) ############
name: __eventTime
path: __eventTime
max_definition_level: 1
max_repetition_level: 0
physical_type: INT96
logical_type: None
converted_type (legacy): NONE

############ Column(key) ############
name: key
path: __messageProperties.key_value.key
max_definition_level: 2
max_repetition_level: 1
physical_type: BYTE_ARRAY
logical_type: String
converted_type (legacy): UTF8

############ Column(value) ############
name: value
path: __messageProperties.key_value.value
max_definition_level: 3
max_repetition_level: 1
physical_type: BYTE_ARRAY
logical_type: String
converted_type (legacy): UTF8

````

### Flink

````
CREATE CATALOG pulsar WITH (
   'type' = 'pulsar',
   'service-url' = 'pulsar://pulsar1:6650',
   'admin-url' = 'http://pulsar1:8080',
   'format' = 'json'
);

USE CATALOG pulsar;

SHOW TABLES;

Flink SQL> describe garden3;
+------------------+--------+------+-----+--------+-----------+
|             name |   type | null | key | extras | watermark |
+------------------+--------+------+-----+--------+-----------+
|              cpu |  FLOAT | true |     |        |           |
|        diskusage | STRING | true |     |        |           |
|          endtime | STRING | true |     |        |           |
| equivalentco2ppm | STRING | true |     |        |           |
|             host | STRING | true |     |        |           |
|         hostname | STRING | true |     |        |           |
|        ipaddress | STRING | true |     |        |           |
|       macaddress | STRING | true |     |        |           |
|           memory |  FLOAT | true |     |        |           |
|            rowid | STRING | true |     |        |           |
|          runtime |    INT | true |     |        |           |
|        starttime | STRING | true |     |        |           |
|       systemtime | STRING | true |     |        |           |
|      totalvocppb | STRING | true |     |        |           |
|               ts |    INT | true |     |        |           |
|             uuid | STRING | true |     |        |           |
+------------------+--------+------+-----+--------+-----------+
16 rows in set

select equivalentco2ppm, totalvocppb, cpu, starttime, systemtime, ts, cpu, diskusage, endtime, memory, uuid from garden3;

select max(equivalentco2ppm) as MaxCO2, max(totalvocppb) as MaxVocPPB from garden3;


// TODO

Add your own table

  publishTime TIMESTAMP(3) METADATA,
  WATERMARK FOR publishTime AS publishTime - INTERVAL '5' SECOND
  

````

![Flink](https://github.com/tspannhw/FLiP-Py-Pi-GasThermal/blob/main/flinksqlairquality.jpg?raw=true)
![Flink2](https://github.com/tspannhw/FLiP-Py-Pi-GasThermal/blob/main/flinksqlairqualityrowsummary.jpg?raw=true)
![Flink3](https://github.com/tspannhw/FLiP-Py-Pi-GasThermal/blob/main/flinksqlairrows.jpg?raw=true)



### Apache NiFi (FLiPN)

* Choose a processor from the palette

![ShowNiFi](https://github.com/tspannhw/FLiP-Py-Pi-GasThermal/blob/main/NIFIpulsarProcessorSelection.jpg?raw=true)

* Consume messages from Apache Pulsar

![ConsumePulsar](https://github.com/tspannhw/FLiP-Py-Pi-GasThermal/blob/main/consumepulsar.jpg?raw=true)


### MongoDB 

````
mongo -u username1 -p password1 --authenticationDatabase admin pulsar1:27017/inventory

show databases

db.createCollection("garden3")

show collections

db.garden3.find().pretty()

{
        "_id" : ObjectId("622f7315f99b9a338d60592f"),
        "cpu" : 0,
        "diskusage" : "101615.9 MB",
        "endtime" : "1647276083.2033532",
        "equivalentco2ppm" : "  407",
        "host" : "garden3",
        "hostname" : "garden3",
        "ipaddress" : "192.168.1.199",
        "macaddress" : "dc:a6:32:32:98:20",
        "memory" : 8.8,
        "rowid" : "20220314164123_0e19c5e6-45f5-405e-bd93-9aed05b37630",
        "runtime" : 0,
        "starttime" : "03/14/2022 12:41:23",
        "systemtime" : "03/14/2022 12:41:24",
        "totalvocppb" : "  5",
        "ts" : 1647276084,
        "uuid" : "garden3_uuid_xrl_20220314164123"
}

````

![mongo](https://github.com/tspannhw/FLiP-Py-Pi-GasThermal/blob/main/mongodbrow.jpg?raw=true)

### References

* https://pypi.org/project/parquet-tools/
* https://nightlies.apache.org/flink/flink-docs-release-1.14/docs/dev/table/sqlclient/
* https://github.com/tspannhw/StreamingAnalyticsUsingFlinkSQL/
* https://nightlies.apache.org/flink/flink-docs-release-1.14/docs/connectors/datastream/pulsar/
* https://shop.pimoroni.com/products/sgp30-air-quality-sensor-breakout?variant=30924091719763
* https://shop.pimoroni.com/products/mlx90640-thermal-camera-breakout?variant=12536948654163
* https://github.com/tspannhw/minifi-gasthermal
* https://dev.to/tspannhw/cloudera-edge2ai-minifi-java-agent-with-raspberry-pi-and-thermal-camera-and-air-quality-sensor-part-1-3oo9
* https://www.datainmotion.dev/2020/01/cloudera-edge2ai-minifi-java-agent-with.html
* https://github.com/tspannhw/FLiP-Pi-Thermal
* https://github.com/pimoroni/mlx90640-library

### Additional Heat Images

![hot](https://github.com/tspannhw/FLiP-Py-Pi-GasThermal/blob/main/mlx90640-2022-03-14-12-03-11.gif?raw=true)
![hot2](https://github.com/tspannhw/FLiP-Py-Pi-GasThermal/blob/main/mlx90640-2022-03-14-12-03-27.gif?raw=true)
![more3](https://github.com/tspannhw/FLiP-Py-Pi-GasThermal/blob/main/mlx90640-2022-03-14-12-03-37.gif?raw=true)
![doesanyonereadthis4](https://github.com/tspannhw/FLiP-Py-Pi-GasThermal/blob/main/mlx90640-2022-03-14-12-38-50.gif?raw=true)

