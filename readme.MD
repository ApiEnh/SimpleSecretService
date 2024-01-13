# LogReader

Authors: 
  [Peter Ashley](https://www.linkedin.com/in/petersouleashley/)

The purpose of this repository is to experment with ML AI based log ingestion and recognition, in particular attempting to use fast.ai deep learning more that traditional methods (e.g. word frequency features) for use cases of log information processsing. 

Use Case:
- As a skilled security engineer, I want to make a custom integration for a device's log information, so that it may be processed in a standardized way by using known security information schemas. For example, use a stardard schema with various logs to write an analytic to alert on N+ failed login attempts followed by success.

Example Log: 

Authentication request succeeded syslog from Fortinet NAC:
02-28-2014 08:16:04 Auth.Notice 192.168.34.31 Feb 27 22:16:14 : 2014/02/27 22:16:14 EST,1,545570,Login Success,0,12,,,,,User root logged in.

Requirements:
- Assists a user in analyzing and constructing a log parser to turn characters into actionable information.
- Takes in device logs, identifies log type, field/entity types and then proposes a relevant schema and field mapping.

## Experiment 1 : Identify log format type (syslog, CEF, etc.) 

Log format identification was accomplished most simply with regex matching as many of the logs have formats that can be identified by signature. Sample python code was generated in a notebook that can be run on kaggle to identify the type of log.

- Kaggle URL	: https://www.kaggle.com/code/peterashley/determinelogtype
- notebook		: notebooks\determinelogtype.ipynb
- test data		: TrainingSources\LogfilesByType.csv

## Reference:
- https://ossec.net/docs/log_samples/
- https://github.com/logpai/loghub
- https://docs.ctpx.secureworks.com/integration/customParsers/schema_antivirus/




  
