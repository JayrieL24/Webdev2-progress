-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 24, 2024 at 01:38 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `gearguards`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `Admin_ID` bigint(255) NOT NULL,
  `ID` varchar(30) NOT NULL,
  `Lab_Assigned` varchar(255) NOT NULL,
  `Name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`Admin_ID`, `ID`, `Lab_Assigned`, `Name`) VALUES
(8, '01', 'Faculty', 'Clyde Chester Balaman'),
(9, '02', 'Faculty', 'Jenn Leana Fernandez'),
(10, '03', 'Faculty', 'Rogelio Badiang'),
(11, '04', 'Faculty', 'Cris John David Manero'),
(12, '05', 'Faculty', 'Michel Bolo');

-- --------------------------------------------------------

--
-- Table structure for table `borrowedtransaction`
--

CREATE TABLE `borrowedtransaction` (
  `TransactionID` bigint(255) NOT NULL,
  `ItemID` bigint(255) NOT NULL,
  `ID` varchar(30) NOT NULL,
  `BorrowedDate` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `borrower`
--

CREATE TABLE `borrower` (
  `BorrowerID` bigint(255) NOT NULL,
  `ID` varchar(30) NOT NULL,
  `Borrowed_Date` datetime(6) NOT NULL,
  `Status` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `borrower`
--

INSERT INTO `borrower` (`BorrowerID`, `ID`, `Borrowed_Date`, `Status`) VALUES
(10, '220000001342', '2024-03-24 00:00:00.000000', 'Borrowing'),
(11, '220000001163', '2024-03-24 00:00:00.000000', 'Available'),
(12, '01', '2024-03-24 00:00:00.000000', 'Borrowing'),
(13, '220000001586', '2024-03-24 00:00:00.000000', 'Borrowing'),
(14, '190000001035', '2024-03-24 19:09:04.000000', 'Available');

-- --------------------------------------------------------

--
-- Table structure for table `item`
--

CREATE TABLE `item` (
  `ItemName` varchar(255) NOT NULL,
  `ItemID` bigint(255) NOT NULL,
  `FromLab` varchar(255) NOT NULL,
  `ItemDescription` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `item`
--

INSERT INTO `item` (`ItemName`, `ItemID`, `FromLab`, `ItemDescription`) VALUES
('KeyBoard', 3, 'IOT-LAB', 'Hardware'),
('Ethernet Cable', 4, 'IOT-LAB', 'Cable'),
('KEVLER JL-15PA Portable speaker', 5, 'IOT-LAB', 'Speaker'),
('CD Cage', 6, 'IOT-LAB', 'Drive'),
('Extention Cable', 7, 'IOT-LAB', 'Cable'),
('Headset', 8, 'IOT-LAB', 'Hardware'),
('Router', 9, 'IOT-LAB', 'Hardware'),
('VGA-to-HDMI', 11, 'IOT-LAB', 'Converter');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `ID` varchar(30) NOT NULL,
  `Course` varchar(255) DEFAULT NULL,
  `Name` varchar(255) NOT NULL,
  `Department` varchar(255) NOT NULL,
  `Role` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`ID`, `Course`, `Name`, `Department`, `Role`) VALUES
('01', NULL, 'Clyde Chester Balaman', 'CCS', 'Personnel'),
('02', NULL, 'Jenn Leana Fernandez', 'CCS', 'Personnel'),
('03', NULL, 'Rogelio Badiang', 'CCS', 'Personnel'),
('04', NULL, 'Cris John David Manero', 'CCS', 'Personnel'),
('05', NULL, 'Michel Bolo\r\n', 'CSS', 'Personnel'),
('190000001035', 'BSIT', 'Ian Labonete', 'CSS', 'Student'),
('220000000989', 'BSCS', 'Princess Micah Espinosa', 'CSS', 'Student'),
('220000001044', 'BSCS', 'Wilfredo Marinay Jr.', 'CCS', 'Student'),
('220000001163', 'BSCS', 'Andre Jose Ruiz', 'CCS', 'Student'),
('220000001342', 'BSCS', 'Jayci Gabriel Acuña', 'CCS', 'Student'),
('220000001551', 'BSIT', 'Jan Kurt Gerongco', 'CCS', 'Student'),
('220000001586', 'BSCS', 'Riggs Harvey Ybañez', 'CCS', 'Student'),
('220000001713', 'BSCS', 'Zyle Adam Doctolero', 'CCS', 'Student');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`Admin_ID`),
  ADD KEY `personnel_to_admin` (`ID`);

--
-- Indexes for table `borrowedtransaction`
--
ALTER TABLE `borrowedtransaction`
  ADD PRIMARY KEY (`TransactionID`),
  ADD KEY `Item_to_BorrowedItem` (`ItemID`),
  ADD KEY `borrower_to_borrowedtransaction` (`ID`);

--
-- Indexes for table `borrower`
--
ALTER TABLE `borrower`
  ADD PRIMARY KEY (`BorrowerID`),
  ADD KEY `user_to_borrower` (`ID`);

--
-- Indexes for table `item`
--
ALTER TABLE `item`
  ADD PRIMARY KEY (`ItemID`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `Admin_ID` bigint(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `borrowedtransaction`
--
ALTER TABLE `borrowedtransaction`
  MODIFY `TransactionID` bigint(255) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `borrower`
--
ALTER TABLE `borrower`
  MODIFY `BorrowerID` bigint(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `item`
--
ALTER TABLE `item`
  MODIFY `ItemID` bigint(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `admin`
--
ALTER TABLE `admin`
  ADD CONSTRAINT `personnel_to_admin` FOREIGN KEY (`ID`) REFERENCES `user` (`ID`);

--
-- Constraints for table `borrowedtransaction`
--
ALTER TABLE `borrowedtransaction`
  ADD CONSTRAINT `Item_to_BorrowedItem` FOREIGN KEY (`ItemID`) REFERENCES `item` (`ItemID`),
  ADD CONSTRAINT `borrower_to_borrowedtransaction` FOREIGN KEY (`ID`) REFERENCES `borrower` (`ID`);

--
-- Constraints for table `borrower`
--
ALTER TABLE `borrower`
  ADD CONSTRAINT `user_to_borrower` FOREIGN KEY (`ID`) REFERENCES `user` (`ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
