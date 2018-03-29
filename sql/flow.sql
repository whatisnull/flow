/*
Navicat MySQL Data Transfer

Source Server         : 192.168.1.110
Source Server Version : 50631
Source Host           : 192.168.1.110:3306
Source Database       : flow

Target Server Type    : MYSQL
Target Server Version : 50631
File Encoding         : 65001

Date: 2017-06-05 23:22:18
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for flow_control
-- ----------------------------
DROP TABLE IF EXISTS `flow_control`;
CREATE TABLE `flow_control` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `fid` bigint(20) NOT NULL,
  `host` varchar(255) NOT NULL,
  `ratio` smallint(4) NOT NULL DEFAULT '100',
  `status` smallint(4) NOT NULL DEFAULT '0',
  `is_default` smallint(4) NOT NULL DEFAULT '0',
  `fid_desc` varchar(255) DEFAULT NULL,
  `create_time` timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `update_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `fid` (`fid`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of flow_control
-- ----------------------------

-- ----------------------------
-- Table structure for flow_dict
-- ----------------------------
DROP TABLE IF EXISTS `flow_dict`;
CREATE TABLE `flow_dict` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `sign` varchar(4) NOT NULL,
  `fid` bigint(20) NOT NULL DEFAULT '0',
  `create_time` timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `update_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `sign` (`sign`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of flow_dict
-- ----------------------------
INSERT INTO `flow_dict` VALUES ('1', '00', '0', '2017-06-04 01:23:42', '2017-06-04 01:23:42');
INSERT INTO `flow_dict` VALUES ('2', '01', '0', '2017-06-04 01:23:42', '2017-06-04 01:23:42');
INSERT INTO `flow_dict` VALUES ('3', '02', '0', '2017-06-04 01:23:42', '2017-06-04 01:23:42');
INSERT INTO `flow_dict` VALUES ('4', '03', '0', '2017-06-04 01:23:42', '2017-06-04 01:23:42');
INSERT INTO `flow_dict` VALUES ('5', '04', '0', '2017-06-04 01:23:42', '2017-06-04 01:23:42');
INSERT INTO `flow_dict` VALUES ('6', '05', '0', '2017-06-04 01:23:42', '2017-06-04 01:23:42');
INSERT INTO `flow_dict` VALUES ('7', '06', '0', '2017-06-04 01:23:43', '2017-06-04 01:23:43');
INSERT INTO `flow_dict` VALUES ('8', '07', '0', '2017-06-04 01:23:43', '2017-06-04 01:23:43');
INSERT INTO `flow_dict` VALUES ('9', '08', '0', '2017-06-04 01:23:43', '2017-06-04 01:23:43');
INSERT INTO `flow_dict` VALUES ('10', '09', '0', '2017-06-04 01:23:43', '2017-06-04 01:23:43');
INSERT INTO `flow_dict` VALUES ('11', '10', '0', '2017-06-04 01:23:43', '2017-06-04 01:23:43');
INSERT INTO `flow_dict` VALUES ('12', '11', '0', '2017-06-04 01:23:43', '2017-06-04 01:23:43');
INSERT INTO `flow_dict` VALUES ('13', '12', '0', '2017-06-04 01:23:43', '2017-06-04 01:23:43');
INSERT INTO `flow_dict` VALUES ('14', '13', '0', '2017-06-04 01:23:43', '2017-06-04 01:23:43');
INSERT INTO `flow_dict` VALUES ('15', '14', '0', '2017-06-04 01:23:43', '2017-06-04 01:23:43');
INSERT INTO `flow_dict` VALUES ('16', '15', '0', '2017-06-04 01:23:43', '2017-06-04 01:23:43');
INSERT INTO `flow_dict` VALUES ('17', '16', '0', '2017-06-04 01:23:43', '2017-06-04 01:23:43');
INSERT INTO `flow_dict` VALUES ('18', '17', '0', '2017-06-04 01:23:43', '2017-06-04 01:23:43');
INSERT INTO `flow_dict` VALUES ('19', '18', '0', '2017-06-04 01:23:43', '2017-06-04 01:23:43');
INSERT INTO `flow_dict` VALUES ('20', '19', '0', '2017-06-04 01:23:43', '2017-06-04 01:23:43');
INSERT INTO `flow_dict` VALUES ('21', '20', '0', '2017-06-04 01:23:43', '2017-06-04 01:23:43');
INSERT INTO `flow_dict` VALUES ('22', '21', '0', '2017-06-04 01:23:43', '2017-06-04 01:23:43');
INSERT INTO `flow_dict` VALUES ('23', '22', '0', '2017-06-04 01:23:43', '2017-06-04 01:23:43');
INSERT INTO `flow_dict` VALUES ('24', '23', '0', '2017-06-04 01:23:43', '2017-06-04 01:23:43');
INSERT INTO `flow_dict` VALUES ('25', '24', '0', '2017-06-04 01:23:44', '2017-06-04 01:23:44');
INSERT INTO `flow_dict` VALUES ('26', '25', '0', '2017-06-04 01:23:44', '2017-06-04 01:23:44');
INSERT INTO `flow_dict` VALUES ('27', '26', '0', '2017-06-04 01:23:44', '2017-06-04 01:23:44');
INSERT INTO `flow_dict` VALUES ('28', '27', '0', '2017-06-04 01:23:44', '2017-06-04 01:23:44');
INSERT INTO `flow_dict` VALUES ('29', '28', '0', '2017-06-04 01:23:44', '2017-06-04 01:23:44');
INSERT INTO `flow_dict` VALUES ('30', '29', '0', '2017-06-04 01:23:44', '2017-06-04 01:23:44');
INSERT INTO `flow_dict` VALUES ('31', '30', '0', '2017-06-04 01:23:44', '2017-06-04 01:23:44');
INSERT INTO `flow_dict` VALUES ('32', '31', '0', '2017-06-04 01:23:44', '2017-06-04 01:23:44');
INSERT INTO `flow_dict` VALUES ('33', '32', '0', '2017-06-04 01:23:44', '2017-06-04 01:23:44');
INSERT INTO `flow_dict` VALUES ('34', '33', '0', '2017-06-04 01:23:44', '2017-06-04 01:23:44');
INSERT INTO `flow_dict` VALUES ('35', '34', '0', '2017-06-04 01:23:44', '2017-06-04 01:23:44');
INSERT INTO `flow_dict` VALUES ('36', '35', '0', '2017-06-04 01:23:44', '2017-06-04 01:23:44');
INSERT INTO `flow_dict` VALUES ('37', '36', '0', '2017-06-04 01:23:44', '2017-06-04 01:23:44');
INSERT INTO `flow_dict` VALUES ('38', '37', '0', '2017-06-04 01:23:44', '2017-06-04 01:23:44');
INSERT INTO `flow_dict` VALUES ('39', '38', '0', '2017-06-04 01:23:44', '2017-06-04 01:23:44');
INSERT INTO `flow_dict` VALUES ('40', '39', '0', '2017-06-04 01:23:44', '2017-06-04 01:23:44');
INSERT INTO `flow_dict` VALUES ('41', '40', '0', '2017-06-04 01:23:44', '2017-06-04 01:23:44');
INSERT INTO `flow_dict` VALUES ('42', '41', '0', '2017-06-04 01:23:44', '2017-06-04 01:23:44');
INSERT INTO `flow_dict` VALUES ('43', '42', '0', '2017-06-04 01:23:44', '2017-06-04 01:23:44');
INSERT INTO `flow_dict` VALUES ('44', '43', '0', '2017-06-04 01:23:44', '2017-06-04 01:23:44');
INSERT INTO `flow_dict` VALUES ('45', '44', '0', '2017-06-04 01:23:44', '2017-06-04 01:23:44');
INSERT INTO `flow_dict` VALUES ('46', '45', '0', '2017-06-04 01:23:44', '2017-06-04 01:23:44');
INSERT INTO `flow_dict` VALUES ('47', '46', '0', '2017-06-04 01:23:45', '2017-06-04 01:23:45');
INSERT INTO `flow_dict` VALUES ('48', '47', '0', '2017-06-04 01:23:45', '2017-06-04 01:23:45');
INSERT INTO `flow_dict` VALUES ('49', '48', '0', '2017-06-04 01:23:45', '2017-06-04 01:23:45');
INSERT INTO `flow_dict` VALUES ('50', '49', '0', '2017-06-04 01:23:45', '2017-06-04 01:23:45');
INSERT INTO `flow_dict` VALUES ('51', '50', '0', '2017-06-04 01:23:45', '2017-06-04 01:23:45');
INSERT INTO `flow_dict` VALUES ('52', '51', '0', '2017-06-04 01:23:45', '2017-06-04 01:23:45');
INSERT INTO `flow_dict` VALUES ('53', '52', '0', '2017-06-04 01:23:45', '2017-06-04 01:23:45');
INSERT INTO `flow_dict` VALUES ('54', '53', '0', '2017-06-04 01:23:45', '2017-06-04 01:23:45');
INSERT INTO `flow_dict` VALUES ('55', '54', '0', '2017-06-04 01:23:45', '2017-06-04 01:23:45');
INSERT INTO `flow_dict` VALUES ('56', '55', '0', '2017-06-04 01:23:45', '2017-06-04 01:23:45');
INSERT INTO `flow_dict` VALUES ('57', '56', '0', '2017-06-04 01:23:45', '2017-06-04 01:23:45');
INSERT INTO `flow_dict` VALUES ('58', '57', '0', '2017-06-04 01:23:45', '2017-06-04 01:23:45');
INSERT INTO `flow_dict` VALUES ('59', '58', '0', '2017-06-04 01:23:45', '2017-06-04 01:23:45');
INSERT INTO `flow_dict` VALUES ('60', '59', '0', '2017-06-04 01:23:45', '2017-06-04 01:23:45');
INSERT INTO `flow_dict` VALUES ('61', '60', '0', '2017-06-04 01:23:45', '2017-06-04 01:23:45');
INSERT INTO `flow_dict` VALUES ('62', '61', '0', '2017-06-04 01:23:45', '2017-06-04 01:23:45');
INSERT INTO `flow_dict` VALUES ('63', '62', '0', '2017-06-04 01:23:45', '2017-06-04 01:23:45');
INSERT INTO `flow_dict` VALUES ('64', '63', '0', '2017-06-04 01:23:45', '2017-06-04 01:23:45');
INSERT INTO `flow_dict` VALUES ('65', '64', '0', '2017-06-04 01:23:45', '2017-06-04 01:23:45');
INSERT INTO `flow_dict` VALUES ('66', '65', '0', '2017-06-04 01:23:45', '2017-06-04 01:23:45');
INSERT INTO `flow_dict` VALUES ('67', '66', '0', '2017-06-04 01:23:45', '2017-06-04 01:23:45');
INSERT INTO `flow_dict` VALUES ('68', '67', '0', '2017-06-04 01:23:45', '2017-06-04 01:23:45');
INSERT INTO `flow_dict` VALUES ('69', '68', '0', '2017-06-04 01:23:45', '2017-06-04 01:23:45');
INSERT INTO `flow_dict` VALUES ('70', '69', '0', '2017-06-04 01:23:45', '2017-06-04 01:23:45');
INSERT INTO `flow_dict` VALUES ('71', '70', '0', '2017-06-04 01:23:45', '2017-06-04 01:23:45');
INSERT INTO `flow_dict` VALUES ('72', '71', '0', '2017-06-04 01:23:45', '2017-06-04 01:23:45');
INSERT INTO `flow_dict` VALUES ('73', '72', '0', '2017-06-04 01:23:45', '2017-06-04 01:23:45');
INSERT INTO `flow_dict` VALUES ('74', '73', '0', '2017-06-04 01:23:46', '2017-06-04 01:23:46');
INSERT INTO `flow_dict` VALUES ('75', '74', '0', '2017-06-04 01:23:46', '2017-06-04 01:23:46');
INSERT INTO `flow_dict` VALUES ('76', '75', '0', '2017-06-04 01:23:46', '2017-06-04 01:23:46');
INSERT INTO `flow_dict` VALUES ('77', '76', '0', '2017-06-04 01:23:46', '2017-06-04 01:23:46');
INSERT INTO `flow_dict` VALUES ('78', '77', '0', '2017-06-04 01:23:46', '2017-06-04 01:23:46');
INSERT INTO `flow_dict` VALUES ('79', '78', '0', '2017-06-04 01:23:46', '2017-06-04 01:23:46');
INSERT INTO `flow_dict` VALUES ('80', '79', '0', '2017-06-04 01:23:46', '2017-06-04 01:23:46');
INSERT INTO `flow_dict` VALUES ('81', '80', '0', '2017-06-04 01:23:46', '2017-06-04 01:23:46');
INSERT INTO `flow_dict` VALUES ('82', '81', '0', '2017-06-04 01:23:46', '2017-06-04 01:23:46');
INSERT INTO `flow_dict` VALUES ('83', '82', '0', '2017-06-04 01:23:46', '2017-06-04 01:23:46');
INSERT INTO `flow_dict` VALUES ('84', '83', '0', '2017-06-04 01:23:46', '2017-06-04 01:23:46');
INSERT INTO `flow_dict` VALUES ('85', '84', '0', '2017-06-04 01:23:46', '2017-06-04 01:23:46');
INSERT INTO `flow_dict` VALUES ('86', '85', '0', '2017-06-04 01:23:46', '2017-06-04 01:23:46');
INSERT INTO `flow_dict` VALUES ('87', '86', '0', '2017-06-04 01:23:46', '2017-06-04 01:23:46');
INSERT INTO `flow_dict` VALUES ('88', '87', '0', '2017-06-04 01:23:46', '2017-06-04 01:23:46');
INSERT INTO `flow_dict` VALUES ('89', '88', '0', '2017-06-04 01:23:46', '2017-06-04 01:23:46');
INSERT INTO `flow_dict` VALUES ('90', '89', '0', '2017-06-04 01:23:46', '2017-06-04 01:23:46');
INSERT INTO `flow_dict` VALUES ('91', '90', '0', '2017-06-04 01:23:46', '2017-06-04 01:23:46');
INSERT INTO `flow_dict` VALUES ('92', '91', '0', '2017-06-04 01:23:46', '2017-06-04 01:23:46');
INSERT INTO `flow_dict` VALUES ('93', '92', '0', '2017-06-04 01:23:46', '2017-06-04 01:23:46');
INSERT INTO `flow_dict` VALUES ('94', '93', '0', '2017-06-04 01:23:46', '2017-06-04 01:23:46');
INSERT INTO `flow_dict` VALUES ('95', '94', '0', '2017-06-04 01:23:46', '2017-06-04 01:23:46');
INSERT INTO `flow_dict` VALUES ('96', '95', '0', '2017-06-04 01:23:46', '2017-06-04 01:23:46');
INSERT INTO `flow_dict` VALUES ('97', '96', '0', '2017-06-04 01:23:46', '2017-06-04 01:23:46');
INSERT INTO `flow_dict` VALUES ('98', '97', '0', '2017-06-04 01:23:46', '2017-06-04 01:23:46');
INSERT INTO `flow_dict` VALUES ('99', '98', '0', '2017-06-04 01:23:46', '2017-06-04 01:23:46');
INSERT INTO `flow_dict` VALUES ('100', '99', '0', '2017-06-04 01:23:46', '2017-06-04 01:23:46');
SET FOREIGN_KEY_CHECKS=1;
