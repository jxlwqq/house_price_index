CREATE DATABASE IF NOT EXISTS house;
USE house;
CREATE TABLE IF NOT EXISTS `area` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `area_name` varchar(50) NOT NULL DEFAULT '' COMMENT '区域名',
  `create_time` timestamp NOT NULL DEFAULT '1970-01-02 00:00:00' COMMENT '创建时间',
  `last_update` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '最近更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
CREATE TABLE IF NOT EXISTS `area_code` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `area_id` int(11) NOT NULL DEFAULT '0' COMMENT '区域id',
  `code_type` varchar(50) NOT NULL DEFAULT '' COMMENT '平台类型',
  `area_code` varchar(50) NOT NULL DEFAULT '' COMMENT '区域代码',
  `create_time` timestamp NOT NULL DEFAULT '1970-01-02 00:00:00' COMMENT '创建时间',
  `last_update` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '最近更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
CREATE TABLE IF NOT EXISTS `house_index` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `time_type` varchar(50) NOT NULL DEFAULT '0' COMMENT 'day week month year',
  `time_index` int(11) NOT NULL DEFAULT '0' COMMENT '日期',
  `area_id` int(11) NOT NULL DEFAULT '0' COMMENT '区域id',
  `data_key` varchar(50) NOT NULL DEFAULT '' COMMENT '键名',
  `data_value` decimal(10,4) NOT NULL DEFAULT '0.0000' COMMENT '值',
  `create_time` timestamp NOT NULL DEFAULT '1970-01-02 00:00:00' COMMENT '创建时间',
  `last_update` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '最近修改时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_ticd` (`time_type`,`time_index`,`area_id`,`data_key`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
CREATE TABLE IF NOT EXISTS `origin_data` (
  `area_name` varchar(50) NOT NULL,
  `code_type` varchar(50) NOT NULL DEFAULT '' COMMENT '各平台的区域编码类型',
  `area_code` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
