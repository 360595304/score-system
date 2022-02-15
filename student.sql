/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 80021
 Source Host           : localhost:3306
 Source Schema         : student

 Target Server Type    : MySQL
 Target Server Version : 80021
 File Encoding         : 65001

 Date: 15/02/2022 17:30:26
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for admin
-- ----------------------------
DROP TABLE IF EXISTS `admin`;
CREATE TABLE `admin`  (
  `id` int NOT NULL,
  `username` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `password` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of admin
-- ----------------------------
INSERT INTO `admin` VALUES (1, 'admin', '123456');

-- ----------------------------
-- Table structure for results
-- ----------------------------
DROP TABLE IF EXISTS `results`;
CREATE TABLE `results`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `s_id` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `course` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `score` decimal(10, 2) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `course_id`(`course`) USING BTREE,
  INDEX `sid`(`s_id`) USING BTREE,
  CONSTRAINT `sid` FOREIGN KEY (`s_id`) REFERENCES `student` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 17 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of results
-- ----------------------------
INSERT INTO `results` VALUES (1, '1901', 'C++', 93.00);
INSERT INTO `results` VALUES (2, '1901', 'Java', 89.00);
INSERT INTO `results` VALUES (3, '1901', '数据结构', 89.00);
INSERT INTO `results` VALUES (4, '1901', '算法', 89.00);
INSERT INTO `results` VALUES (5, '1901', 'Python', 89.00);
INSERT INTO `results` VALUES (6, '1902', 'C++', 70.00);
INSERT INTO `results` VALUES (7, '1902', 'Java', 88.00);
INSERT INTO `results` VALUES (8, '1902', '数据结构', 89.00);
INSERT INTO `results` VALUES (9, '1902', 'Python', 89.00);
INSERT INTO `results` VALUES (10, '1902', '算法', 89.00);
INSERT INTO `results` VALUES (11, '1903', 'C++', 77.00);
INSERT INTO `results` VALUES (12, '1903', 'Java', 89.00);
INSERT INTO `results` VALUES (13, '1903', 'Python', 89.00);
INSERT INTO `results` VALUES (14, '1903', '数据结构', 89.00);
INSERT INTO `results` VALUES (15, '1903', '算法', 89.00);
INSERT INTO `results` VALUES (17, '1904', 'C++', 85.00);

-- ----------------------------
-- Table structure for student
-- ----------------------------
DROP TABLE IF EXISTS `student`;
CREATE TABLE `student`  (
  `id` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `password` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '123456',
  `sex` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `college` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `class` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of student
-- ----------------------------
INSERT INTO `student` VALUES ('1901', '张三', '123456', '男', '信工', '软工1901');
INSERT INTO `student` VALUES ('1902', '李四', '123456', '男', '信工', '软工1901');
INSERT INTO `student` VALUES ('1903', '王五', '123456', '男', '信工', '软工1901');
INSERT INTO `student` VALUES ('1904', '哈哈', '123456', '男', '信工', '软工1902');
INSERT INTO `student` VALUES ('1905', '张四', '123456', '男', '艺术', '艺术1901');
INSERT INTO `student` VALUES ('1906', 'abc', '123456', '女', '信工', '网工1901');

SET FOREIGN_KEY_CHECKS = 1;
