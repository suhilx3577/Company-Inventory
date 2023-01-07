-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 02, 2022 at 11:22 AM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `company`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `adminid` int(11) NOT NULL,
  `adminname` varchar(100) NOT NULL,
  `adminpw` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`adminid`, `adminname`, `adminpw`) VALUES
(90012, 'suhil', '123456');

-- --------------------------------------------------------

--
-- Table structure for table `category`
--

CREATE TABLE `category` (
  `cid` varchar(100) NOT NULL,
  `catname` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `category`
--

INSERT INTO `category` (`cid`, `catname`) VALUES
('cat001', 'Sports'),
('M003', 'Hyginee');

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `cusid` varchar(100) NOT NULL,
  `cusname` varchar(100) NOT NULL,
  `cuscont` varchar(100) NOT NULL,
  `cusaddr` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`cusid`, `cusname`, `cuscont`, `cusaddr`) VALUES
('C1002', 'muresh', '8618223298', 'Bangalore, Karnataka');

-- --------------------------------------------------------

--
-- Table structure for table `inventory`
--

CREATE TABLE `inventory` (
  `inventid` varchar(100) NOT NULL,
  `productname` varchar(100) NOT NULL,
  `stockin` int(11) NOT NULL,
  `stockout` int(11) NOT NULL,
  `stockavail` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `inventory`
--

INSERT INTO `inventory` (`inventid`, `productname`, `stockin`, `stockout`, `stockavail`) VALUES
('0012', 'BAT', 200, 90, 140),
('C002', 'Ball', 300, 200, 100),
('N097', 'WICKET', 700, 400, 300);

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

CREATE TABLE `product` (
  `pid` varchar(100) NOT NULL,
  `catname` varchar(100) NOT NULL,
  `pname` varchar(100) NOT NULL,
  `pdesc` varchar(100) NOT NULL,
  `prodqty` int(11) NOT NULL,
  `pprice` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `product`
--

INSERT INTO `product` (`pid`, `catname`, `pname`, `pdesc`, `prodqty`, `pprice`) VALUES
('002', 'Sports', 'Ball', 'This', 10000, '30.00'),
('003', 'Sports', 'Wicket', 'This', 10010, '300'),
('AM0023', 'HYGINEE', 'GGH', 'cghjhg', 3554, '122333'),
('P001', 'Sports', 'Bat', 'This', 1010, '2000');

-- --------------------------------------------------------

--
-- Table structure for table `receiving`
--

CREATE TABLE `receiving` (
  `rdate` varchar(100) NOT NULL,
  `rid` varchar(100) NOT NULL,
  `supname` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `receiving`
--

INSERT INTO `receiving` (`rdate`, `rid`, `supname`) VALUES
('2022-02-22', '80013', 'Supplier3'),
('2022-02-23', '80112', 'Supplier1'),
('2022-08-28', 'P001', 'RACHITHA'),
('2022-08-29', 'R0012', 'RACHITHA');

-- --------------------------------------------------------

--
-- Table structure for table `sales`
--

CREATE TABLE `sales` (
  `sid` varchar(100) NOT NULL,
  `prodid` varchar(100) NOT NULL,
  `cusname` varchar(100) NOT NULL,
  `saleqty` int(11) NOT NULL,
  `sdate` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `sales`
--

INSERT INTO `sales` (`sid`, `prodid`, `cusname`, `saleqty`, `sdate`) VALUES
('S001', 'AM0023', 'RAMESHa', 300, '2022-09-01');

-- --------------------------------------------------------

--
-- Table structure for table `supplier`
--

CREATE TABLE `supplier` (
  `supid` varchar(100) NOT NULL,
  `supname` varchar(100) NOT NULL,
  `supcont` varchar(100) NOT NULL,
  `supaddr` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `supplier`
--

INSERT INTO `supplier` (`supid`, `supname`, `supcont`, `supaddr`) VALUES
('9123', 'Supplier4', '8618223298', 'Bangalore,Karnataka');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`adminid`);

--
-- Indexes for table `category`
--
ALTER TABLE `category`
  ADD PRIMARY KEY (`cid`);

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`cusid`);

--
-- Indexes for table `inventory`
--
ALTER TABLE `inventory`
  ADD PRIMARY KEY (`inventid`);

--
-- Indexes for table `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`pid`);

--
-- Indexes for table `receiving`
--
ALTER TABLE `receiving`
  ADD PRIMARY KEY (`rid`);

--
-- Indexes for table `sales`
--
ALTER TABLE `sales`
  ADD PRIMARY KEY (`sid`);

--
-- Indexes for table `supplier`
--
ALTER TABLE `supplier`
  ADD PRIMARY KEY (`supid`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
