CREATE DATABASE `britecore` /*!40100 DEFAULT CHARACTER SET latin1 */;


USE `britecore`;


CREATE TABLE `client` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fullname` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE `product_area` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE `request` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(45) NOT NULL,
  `description` varchar(255) NOT NULL,
  `client_id` int(11) NOT NULL,
  `client_priority` int(11) NOT NULL,
  `target_date` date NOT NULL,
  `product_area_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_request_client_id_idx` (`client_id`),
  KEY `fk_request_product_area_id_idx` (`product_area_id`),
  CONSTRAINT `fk_request_client_id` FOREIGN KEY (`client_id`) REFERENCES `client` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_request_product_area_id` FOREIGN KEY (`product_area_id`) REFERENCES `product_area` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


INSERT INTO `britecore`.`client`(`fullname`) VALUES
('Client A'),
('Client B'),
('Client C');


INSERT INTO `britecore`.`product_area`(`name`) VALUES
('Policies'),
('Billing'),
('Claims'),
('Reports');

CREATE USER 'britecoreuser'@'localhost' IDENTIFIED BY 'britecorepassword';

GRANT ALL PRIVILEGES ON `britecore`.* TO 'britecoreuser'@'localhost';

FLUSH PRIVILEGES;