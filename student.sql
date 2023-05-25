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

 Date: 25/05/2023 20:50:52
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
-- Table structure for course
-- ----------------------------
DROP TABLE IF EXISTS `course`;
CREATE TABLE `course`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `description` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of course
-- ----------------------------
INSERT INTO `course` VALUES (1, 'C++', '学C++写代码');
INSERT INTO `course` VALUES (2, 'Java', '学Java找个班上');
INSERT INTO `course` VALUES (3, '数据结构', '数据结构是基础啊');
INSERT INTO `course` VALUES (4, '算法', '学算法打比赛');
INSERT INTO `course` VALUES (5, 'Python', '学Python爬虫');
INSERT INTO `course` VALUES (6, '计算机网络', '必学');
INSERT INTO `course` VALUES (7, '数据库', 'MySQL');
INSERT INTO `course` VALUES (8, '操作系统', '操作系统好啊');

-- ----------------------------
-- Table structure for results
-- ----------------------------
DROP TABLE IF EXISTS `results`;
CREATE TABLE `results`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `s_id` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `course_id` int NOT NULL,
  `score` decimal(10, 2) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `course_id`(`course_id`) USING BTREE,
  INDEX `sid`(`s_id`) USING BTREE,
  CONSTRAINT `sid` FOREIGN KEY (`s_id`) REFERENCES `student` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 18 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of results
-- ----------------------------
INSERT INTO `results` VALUES (1, '1901', 1, 93.00);
INSERT INTO `results` VALUES (2, '1901', 2, 89.00);
INSERT INTO `results` VALUES (3, '1901', 3, 89.00);
INSERT INTO `results` VALUES (4, '1901', 4, 89.00);
INSERT INTO `results` VALUES (5, '1901', 5, 89.00);
INSERT INTO `results` VALUES (6, '1902', 1, 70.00);
INSERT INTO `results` VALUES (7, '1902', 2, 88.00);
INSERT INTO `results` VALUES (8, '1902', 3, 81.00);
INSERT INTO `results` VALUES (9, '1902', 5, 89.00);
INSERT INTO `results` VALUES (10, '1902', 4, 89.00);
INSERT INTO `results` VALUES (11, '1903', 1, 77.00);
INSERT INTO `results` VALUES (12, '1903', 2, 89.00);
INSERT INTO `results` VALUES (13, '1903', 5, 89.00);
INSERT INTO `results` VALUES (14, '1903', 3, 89.00);
INSERT INTO `results` VALUES (15, '1903', 4, 89.00);
INSERT INTO `results` VALUES (17, '1904', 1, 80.00);

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
