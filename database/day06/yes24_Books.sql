-- MySQL dump 10.13  Distrib 8.0.40, for macos14 (arm64)
--
-- Host: localhost    Database: yes24
-- ------------------------------------------------------
-- Server version	9.1.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Books`
--

DROP TABLE IF EXISTS `Books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Books` (
  `bookID` int NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `author` varchar(255) DEFAULT NULL,
  `publisher` varchar(255) DEFAULT NULL,
  `publishing` date DEFAULT NULL,
  `rating` decimal(3,1) DEFAULT NULL,
  `review` int DEFAULT NULL,
  `sales` int DEFAULT NULL,
  `price` decimal(10,2) DEFAULT NULL,
  `ranking` int DEFAULT NULL,
  `ranking_weeks` int DEFAULT NULL,
  PRIMARY KEY (`bookID`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Books`
--

LOCK TABLES `Books` WRITE;
/*!40000 ALTER TABLE `Books` DISABLE KEYS */;
INSERT INTO `Books` VALUES (1,'초역 부처의 말','코이케 류노스케 저/박재현 역','포레스트북스','2024-05-30',9.5,206,388866,17800.00,0,1),(2,'소년이 온다','한강 저','창비','2014-05-19',9.7,2786,3165963,15000.00,11,2),(3,'STOP THE STEAL 대법원의 부정선거 은폐기록','도태우, 박주현, 윤용진, 현성삼 공저','스카이','2025-01-20',9.6,187,81030,15000.00,0,0),(4,'행동하지 않으면 인생은 바뀌지 않는다','브라이언 트레이시 저/정지현 역','현대지성','2024-11-19',9.3,122,332592,16900.00,114,4),(5,'하루 한 장 나의 어휘력을 위한 필사 노트','유선경 저','위즈덤하우스','2024-10-23',9.6,587,933234,23800.00,207,5),(6,'어른의 행복은 조용하다','태수 저','페이지2북스','2024-11-04',9.5,97,303168,17800.00,13,6),(7,'채식주의자','한강 저','창비','2022-03-28',9.1,1378,2319375,15000.00,2011,7),(8,'왜 그들만 부자가 되는가','필립 바구스, 안드레아스 마르크바르트 저/배진아 역','북모먼트','2025-01-08',9.7,63,77187,22000.00,2016,8),(9,'작별하지 않는다','한강 저','문학동네','2021-09-09',9.6,1736,1931097,16800.00,201,9),(10,'미국 주식 투자의 정석','최철 저','황금부엉이','2025-01-21',9.6,74,140577,29000.00,2029,10),(11,'2025 큰별쌤 최태성의 별별한국사 기출 500제 한국사능력검정시험 심화(1,2,3급)','최태성 저','이투스북','2024-12-24',10.0,15,192954,19500.00,11,11),(12,'모순','양귀자 저','쓰다','2013-04-01',9.6,1284,428520,13000.00,203,12),(13,'ETS 토익 정기시험 기출문제집 1000 Vol. 4 RC','ETS 저','YBM(와이비엠)','2023-12-20',9.7,354,563595,19800.00,2015,13),(14,'급류','정대건 저','민음사','2022-12-22',9.2,184,183186,14000.00,2039,14),(15,'ETS 토익 정기시험 기출문제집 1000 Vol. 4 LC','ETS 저','YBM(와이비엠)','2023-12-20',9.8,295,530058,19800.00,10018,15),(16,'2025 큰별쌤 최태성의 별별한국사 한국사능력검정시험 심화(1,2,3급) 상','최태성 저','이투스북','2024-12-24',10.0,21,310998,16500.00,2033,16),(17,'2025 큰별쌤 최태성의 별별한국사 한국사능력검정시험 심화(1,2,3급) 하','최태성 저','이투스북','2024-12-24',10.0,14,296133,16000.00,205,17),(18,'마음의 기술','안-엘렌 클레르, 뱅상 트리부 저/구영옥 역','상상스퀘어','2024-11-18',9.1,32,112248,21000.00,205,18),(19,'마흔에 읽는 쇼펜하우어','강용수 저','유노북스','2023-09-07',8.7,734,529746,17000.00,10010,19),(20,'이처럼 사소한 것들','클레어 키건 저/홍한별 역','다산책방','2023-11-27',9.5,638,449238,13800.00,112,20),(21,'퓨처 셀프 30만 부 기념 스페셜 에디션','벤저민 하디 저/최은아 역','상상스퀘어','2024-09-25',9.3,83,230262,22000.00,2022,21),(22,'지금 거신 전화는 대본집 세트','김지운 저','BIRDBOX(버드박스)','2025-03-10',10.0,2,21030,48000.00,208,22),(23,'서랍에 저녁을 넣어 두었다','한강 저','문학과지성사','2013-11-15',9.7,641,782013,12000.00,1001,23),(24,'원피스 ONE PIECE 110','오다 에이이치로 글그림','대원','2025-01-23',9.8,62,71340,6000.00,2014,24);
/*!40000 ALTER TABLE `Books` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-02-01  2:32:53
