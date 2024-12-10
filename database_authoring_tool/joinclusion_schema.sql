-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Εξυπηρετητής: 127.0.0.1
-- Χρόνος δημιουργίας: 22 Ιαν 2024 στις 12:15:09
-- Έκδοση διακομιστή: 10.4.28-MariaDB
-- Έκδοση PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `joinclusion-authoring-tool` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;

USE `joinclusion-authoring-tool`;

--
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Βάση δεδομένων: `joinclusion`
--

-- --------------------------------------------------------

--
-- Δομή πίνακα για τον πίνακα `mods`
--

DROP TABLE IF EXISTS `mods`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;

CREATE TABLE `mods` (
  `id` int(11) NOT NULL,
  `teachers_id` int(11) NOT NULL,
  `mod_name` varchar(20) NOT NULL,
  `number_of_players` int(4) UNSIGNED NOT NULL,
  `mod_timer_active` tinyint(1) NOT NULL,
  `mod_timer_time` int(11) NOT NULL,
  `mode_code` int(4) NOT NULL,
  `mod_json` text NOT NULL,
  `published` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Άδειασμα δεδομένων του πίνακα `mods`
--

INSERT INTO `mods` (`id`, `teachers_id`, `mod_name`, `number_of_players`, `mod_timer_active`, `mod_timer_time`, `mode_code`, `mod_json`, `published`) VALUES
(7, 1, 'Example_01', 3, 0, 5, 4204, '[\n  {\n    \"location\": {\n      \"id\": 0,\n      \"name\": \"Lockers\",\n      \"img\": \"lockers\",\n      \"interactibleAreas\": [\n        {\n          \"interactibleArea\": {\n            \"id\": 0,\n            \"position\": \"bottom-4 left-10\",\n            \"character\": \"none\"\n          }\n        },\n        {\n          \"interactibleArea\": {\n            \"id\": 1,\n            \"position\": \"bottom-4 right-4\",\n            \"character\": {\n              \"id\": 1,\n              \"name\": \"Dennis\",\n              \"img\": \"dennis_full_neutral\",\n              \"topic\": {\n                \"id\": 0,\n                \"src\": \"A\",\n                \"header\": \"We must collect all the gems..\"\n              }\n            }\n          }\n        }\n      ],\n      \"gemInteractibleAreas\": [\n        {\n          \"gemInteractibleArea\": {\n            \"id\": 0,\n            \"position\": \"left-60 bottom-20 top-48\",\n            \"gem\": \"none\"\n          }\n        },\n        {\n          \"gemInteractibleArea\": {\n            \"id\": 1,\n            \"position\": \"bottom-20 right-60 top-48\",\n            \"gem\": {\n              \"id\": 1,\n              \"name\": \"1\",\n              \"img\": \"1\",\n              \"gemTopic\": {\n                \"id\": 1,\n                \"src\": \"B\",\n                \"header\": \"Classmate remains out of the teams\"\n              }\n            }\n          }\n        }\n      ]\n    }\n  },\n  {\n    \"location\": {\n      \"id\": 1,\n      \"name\": \"Math Class\",\n      \"img\": \"math_class\",\n      \"interactibleAreas\": [\n        {\n          \"interactibleArea\": {\n            \"id\": 0,\n            \"position\": \"bottom-4 left-10\",\n            \"character\": \"none\"\n          }\n        },\n        {\n          \"interactibleArea\": {\n            \"id\": 1,\n            \"position\": \"bottom-4 right-4\",\n            \"character\": \"none\"\n          }\n        }\n      ],\n      \"gemInteractibleAreas\": [\n        {\n          \"gemInteractibleArea\": {\n            \"id\": 0,\n            \"position\": \"left-60 bottom-20 top-48\",\n            \"gem\": \"none\"\n          }\n        },\n        {\n          \"gemInteractibleArea\": {\n            \"id\": 1,\n            \"position\": \"bottom-20 right-60 top-48\",\n            \"gem\": \"none\"\n          }\n        }\n      ]\n    }\n  },\n  {\n    \"location\": {\n      \"id\": 2,\n      \"name\": \"Computer Class\",\n      \"img\": \"computer_class\",\n      \"interactibleAreas\": [\n        {\n          \"interactibleArea\": {\n            \"id\": 0,\n            \"position\": \"bottom-4 left-10\",\n            \"character\": \"none\"\n          }\n        },\n        {\n          \"interactibleArea\": {\n            \"id\": 1,\n            \"position\": \"bottom-4 right-4\",\n            \"character\": \"none\"\n          }\n        }\n      ],\n      \"gemInteractibleAreas\": [\n        {\n          \"gemInteractibleArea\": {\n            \"id\": 0,\n            \"position\": \"left-60 bottom-20 top-48\",\n            \"gem\": \"none\"\n          }\n        },\n        {\n          \"gemInteractibleArea\": {\n            \"id\": 1,\n            \"position\": \"bottom-20 right-60 top-48\",\n            \"gem\": \"none\"\n          }\n        }\n      ]\n    }\n  },\n  {\n    \"location\": {\n      \"id\": 3,\n      \"name\": \"Literature Class\",\n      \"img\": \"literature_class\",\n      \"interactibleAreas\": [\n        {\n          \"interactibleArea\": {\n            \"id\": 0,\n            \"position\": \"bottom-4 left-10\",\n            \"character\": \"none\"\n          }\n        },\n        {\n          \"interactibleArea\": {\n            \"id\": 1,\n            \"position\": \"bottom-4 right-4\",\n            \"character\": \"none\"\n          }\n        }\n      ],\n      \"gemInteractibleAreas\": [\n        {\n          \"gemInteractibleArea\": {\n            \"id\": 0,\n            \"position\": \"left-60 bottom-20 top-48\",\n            \"gem\": \"none\"\n          }\n        },\n        {\n          \"gemInteractibleArea\": {\n            \"id\": 1,\n            \"position\": \"bottom-20 right-60 top-48\",\n            \"gem\": \"none\"\n          }\n        }\n      ]\n    }\n  }\n]', 1),
(10, 1, 'Example_02', 3, 1, 3, 5686, '[\n  {\n    \"location\": {\n      \"id\": 0,\n      \"name\": \"Lockers\",\n      \"img\": \"lockers\",\n      \"interactibleAreas\": [\n        {\n          \"interactibleArea\": {\n            \"id\": 0,\n            \"position\": \"bottom-4 left-10\",\n            \"character\": {\n              \"id\": 0,\n              \"name\": \"Tom\",\n              \"img\": \"tom_full_neutral\",\n              \"topic\": {\n                \"id\": 1,\n                \"src\": \"B\",\n                \"header\": \"I am scared.\"\n              }\n            }\n          }\n        },\n        {\n          \"interactibleArea\": {\n            \"id\": 1,\n            \"position\": \"bottom-4 right-4\",\n            \"character\": \"none\"\n          }\n        }\n      ],\n      \"gemInteractibleAreas\": [\n        {\n          \"gemInteractibleArea\": {\n            \"id\": 0,\n            \"position\": \"left-60 bottom-20 top-48\",\n            \"gem\": \"none\"\n          }\n        },\n        {\n          \"gemInteractibleArea\": {\n            \"id\": 1,\n            \"position\": \"bottom-20 right-60 top-48\",\n            \"gem\": \"none\"\n          }\n        }\n      ]\n    }\n  },\n  {\n    \"location\": {\n      \"id\": 1,\n      \"name\": \"Math Class\",\n      \"img\": \"math_class\",\n      \"interactibleAreas\": [\n        {\n          \"interactibleArea\": {\n            \"id\": 0,\n            \"position\": \"bottom-4 left-10\",\n            \"character\": \"none\"\n          }\n        },\n        {\n          \"interactibleArea\": {\n            \"id\": 1,\n            \"position\": \"bottom-4 right-4\",\n            \"character\": \"none\"\n          }\n        }\n      ],\n      \"gemInteractibleAreas\": [\n        {\n          \"gemInteractibleArea\": {\n            \"id\": 0,\n            \"position\": \"left-60 bottom-20 top-48\",\n            \"gem\": {\n              \"id\": 2,\n              \"name\": \"2\",\n              \"img\": \"2\",\n              \"gemTopic\": {\n                \"id\": 2,\n                \"src\": \"C\",\n                \"header\": \"A group of children is fighting with a classmate\"\n              }\n            }\n          }\n        },\n        {\n          \"gemInteractibleArea\": {\n            \"id\": 1,\n            \"position\": \"bottom-20 right-60 top-48\",\n            \"gem\": \"none\"\n          }\n        }\n      ]\n    }\n  },\n  {\n    \"location\": {\n      \"id\": 2,\n      \"name\": \"Computer Class\",\n      \"img\": \"computer_class\",\n      \"interactibleAreas\": [\n        {\n          \"interactibleArea\": {\n            \"id\": 0,\n            \"position\": \"bottom-4 left-10\",\n            \"character\": \"none\"\n          }\n        },\n        {\n          \"interactibleArea\": {\n            \"id\": 1,\n            \"position\": \"bottom-4 right-4\",\n            \"character\": \"none\"\n          }\n        }\n      ],\n      \"gemInteractibleAreas\": [\n        {\n          \"gemInteractibleArea\": {\n            \"id\": 0,\n            \"position\": \"left-60 bottom-20 top-48\",\n            \"gem\": \"none\"\n          }\n        },\n        {\n          \"gemInteractibleArea\": {\n            \"id\": 1,\n            \"position\": \"bottom-20 right-60 top-48\",\n            \"gem\": \"none\"\n          }\n        }\n      ]\n    }\n  },\n  {\n    \"location\": {\n      \"id\": 3,\n      \"name\": \"Literature Class\",\n      \"img\": \"literature_class\",\n      \"interactibleAreas\": [\n        {\n          \"interactibleArea\": {\n            \"id\": 0,\n            \"position\": \"bottom-4 left-10\",\n            \"character\": \"none\"\n          }\n        },\n        {\n          \"interactibleArea\": {\n            \"id\": 1,\n            \"position\": \"bottom-4 right-4\",\n            \"character\": \"none\"\n          }\n        }\n      ],\n      \"gemInteractibleAreas\": [\n        {\n          \"gemInteractibleArea\": {\n            \"id\": 0,\n            \"position\": \"left-60 bottom-20 top-48\",\n            \"gem\": \"none\"\n          }\n        },\n        {\n          \"gemInteractibleArea\": {\n            \"id\": 1,\n            \"position\": \"bottom-20 right-60 top-48\",\n            \"gem\": \"none\"\n          }\n        }\n      ]\n    }\n  }\n]', 1),
(11, 1, 'Example_03', 3, 0, 3, 7183, '[\n  {\n    \"location\": {\n      \"id\": 0,\n      \"name\": \"Lockers\",\n      \"img\": \"lockers\",\n      \"interactibleAreas\": [\n        {\n          \"interactibleArea\": {\n            \"id\": 0,\n            \"position\": \"bottom-4 left-10\",\n            \"character\": {\n              \"id\": 0,\n              \"name\": \"Tom\",\n              \"img\": \"tom_full_neutral\",\n              \"topic\": {\n                \"id\": 1,\n                \"src\": \"B\",\n                \"header\": \"I am scared.\"\n              }\n            }\n          }\n        },\n        {\n          \"interactibleArea\": {\n            \"id\": 1,\n            \"position\": \"bottom-4 right-4\",\n            \"character\": \"none\"\n          }\n        }\n      ],\n      \"gemInteractibleAreas\": [\n        {\n          \"gemInteractibleArea\": {\n            \"id\": 0,\n            \"position\": \"left-60 bottom-20 top-48\",\n            \"gem\": {\n              \"id\": 0,\n              \"name\": \"0\",\n              \"img\": \"0\",\n              \"gemTopic\": {\n                \"id\": 5,\n                \"src\": \"F\",\n                \"header\": \"Project Leader\"\n              }\n            }\n          }\n        },\n        {\n          \"gemInteractibleArea\": {\n            \"id\": 1,\n            \"position\": \"bottom-20 right-60 top-48\",\n            \"gem\": {\n              \"id\": 1,\n              \"name\": \"1\",\n              \"img\": \"1\",\n              \"gemTopic\": {\n                \"id\": 6,\n                \"src\": \"G\",\n                \"header\": \"Bulling a classmate\"\n              }\n            }\n          }\n        }\n      ]\n    }\n  },\n  {\n    \"location\": {\n      \"id\": 1,\n      \"name\": \"Math Class\",\n      \"img\": \"math_class\",\n      \"interactibleAreas\": [\n        {\n          \"interactibleArea\": {\n            \"id\": 0,\n            \"position\": \"bottom-4 left-10\",\n            \"character\": \"none\"\n          }\n        },\n        {\n          \"interactibleArea\": {\n            \"id\": 1,\n            \"position\": \"bottom-4 right-4\",\n            \"character\": \"none\"\n          }\n        }\n      ],\n      \"gemInteractibleAreas\": [\n        {\n          \"gemInteractibleArea\": {\n            \"id\": 0,\n            \"position\": \"left-60 bottom-20 top-48\",\n            \"gem\": {\n              \"id\": 2,\n              \"name\": \"2\",\n              \"img\": \"2\",\n              \"gemTopic\": {\n                \"id\": 7,\n                \"src\": \"H\",\n                \"header\": \"Traditional food\"\n              }\n            }\n          }\n        },\n        {\n          \"gemInteractibleArea\": {\n            \"id\": 1,\n            \"position\": \"bottom-20 right-60 top-48\",\n            \"gem\": {\n              \"id\": 3,\n              \"name\": \"3\",\n              \"img\": \"3\",\n              \"gemTopic\": {\n                \"id\": 8,\n                \"src\": \"I\",\n                \"header\": \"Eating alone\"\n              }\n            }\n          }\n        }\n      ]\n    }\n  },\n  {\n    \"location\": {\n      \"id\": 2,\n      \"name\": \"Computer Class\",\n      \"img\": \"computer_class\",\n      \"interactibleAreas\": [\n        {\n          \"interactibleArea\": {\n            \"id\": 0,\n            \"position\": \"bottom-4 left-10\",\n            \"character\": \"none\"\n          }\n        },\n        {\n          \"interactibleArea\": {\n            \"id\": 1,\n            \"position\": \"bottom-4 right-4\",\n            \"character\": \"none\"\n          }\n        }\n      ],\n      \"gemInteractibleAreas\": [\n        {\n          \"gemInteractibleArea\": {\n            \"id\": 0,\n            \"position\": \"left-60 bottom-20 top-48\",\n            \"gem\": {\n              \"id\": 4,\n              \"name\": \"4\",\n              \"img\": \"4\",\n              \"gemTopic\": {\n                \"id\": 9,\n                \"src\": \"J\",\n                \"header\": \"Islamic Holiday\"\n              }\n            }\n          }\n        },\n        {\n          \"gemInteractibleArea\": {\n            \"id\": 1,\n            \"position\": \"bottom-20 right-60 top-48\",\n            \"gem\": \"none\"\n          }\n        }\n      ]\n    }\n  },\n  {\n    \"location\": {\n      \"id\": 3,\n      \"name\": \"Literature Class\",\n      \"img\": \"literature_class\",\n      \"interactibleAreas\": [\n        {\n          \"interactibleArea\": {\n            \"id\": 0,\n            \"position\": \"bottom-4 left-10\",\n            \"character\": \"none\"\n          }\n        },\n        {\n          \"interactibleArea\": {\n            \"id\": 1,\n            \"position\": \"bottom-4 right-4\",\n            \"character\": \"none\"\n          }\n        }\n      ],\n      \"gemInteractibleAreas\": [\n        {\n          \"gemInteractibleArea\": {\n            \"id\": 0,\n            \"position\": \"left-60 bottom-20 top-48\",\n            \"gem\": \"none\"\n          }\n        },\n        {\n          \"gemInteractibleArea\": {\n            \"id\": 1,\n            \"position\": \"bottom-20 right-60 top-48\",\n            \"gem\": \"none\"\n          }\n        }\n      ]\n    }\n  }\n]', 1);

-- --------------------------------------------------------

--
-- Δομή πίνακα για τον πίνακα `teachers`
--

DROP TABLE IF EXISTS `teachers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;

CREATE TABLE `teachers` (
  `id` int(11) NOT NULL,
  `username` varchar(20) NOT NULL,
  `pwd` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Άδειασμα δεδομένων του πίνακα `teachers`
--

INSERT INTO `teachers` (`id`, `username`, `pwd`) VALUES
(1, 'admin', 'admin');
INSERT INTO `teachers` (`id`, `username`, `pwd`) VALUES
(2, 'teacher1', 'teacher1');
INSERT INTO `teachers` (`id`, `username`, `pwd`) VALUES
(3, 'teacher2', 'teacher2');
INSERT INTO `teachers` (`id`, `username`, `pwd`) VALUES
(4, 'teacher3', 'teacher3');
INSERT INTO `teachers` (`id`, `username`, `pwd`) VALUES
(5, 'teacher4', 'teacher4');
INSERT INTO `teachers` (`id`, `username`, `pwd`) VALUES
(6, 'teacher5', 'teacher5');
INSERT INTO `teachers` (`id`, `username`, `pwd`) VALUES
(7, 'teacher6', 'teacher6');
INSERT INTO `teachers` (`id`, `username`, `pwd`) VALUES
(8, 'teacher7', 'teacher7');
INSERT INTO `teachers` (`id`, `username`, `pwd`) VALUES
(9, 'teacher8', 'teacher8');
INSERT INTO `teachers` (`id`, `username`, `pwd`) VALUES
(10, 'teacher9', 'teacher9');
INSERT INTO `teachers` (`id`, `username`, `pwd`) VALUES
(11, 'teacher10', 'teacher10');

--
-- Ευρετήρια για άχρηστους πίνακες
--

--
-- Ευρετήρια για πίνακα `mods`
--
ALTER TABLE `mods`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `mode_code` (`mode_code`);

--
-- Ευρετήρια για πίνακα `teachers`
--
ALTER TABLE `teachers`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT για άχρηστους πίνακες
--

--
-- AUTO_INCREMENT για πίνακα `mods`
--
ALTER TABLE `mods`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT για πίνακα `teachers`
--
ALTER TABLE `teachers`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
