-- ====================================
-- 1. Buat Database Baru
-- ====================================
CREATE DATABASE data_kependudukan_indonesia;
USE data_kependudukan_indonesia;

-- ====================================
-- 2. Tabel households
-- ====================================
CREATE TABLE households (
    id INT AUTO_INCREMENT PRIMARY KEY,
    head_name VARCHAR(100) NOT NULL,
    head_age INT NOT NULL,
    education_level VARCHAR(50),
    marital_status VARCHAR(20),
    num_children INT,
    house_size_m2 INT,
    monthly_expense_estimate DECIMAL(12,2)
);

-- ====================================
-- 3. Tabel financial_records
-- ====================================
CREATE TABLE financial_records (
    id INT AUTO_INCREMENT PRIMARY KEY,
    household_id INT NOT NULL,
    main_job VARCHAR(100),
    monthly_income DECIMAL(12,2),
    monthly_expense DECIMAL(12,2),
    savings DECIMAL(12,2),
    debt DECIMAL(12,2),
    FOREIGN KEY (household_id) REFERENCES households(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- ====================================
-- 4. Data households (40 baris)
-- ====================================
INSERT INTO households
(head_name, head_age, education_level, marital_status, num_children, house_size_m2, monthly_expense_estimate)
VALUES
('Agus Setiawan',45,'Sarjana','Menikah',3,120,5200000),
('Bambang Prakoso',52,'SMA','Menikah',2,150,4700000),
('Cindy Maharani',34,'Magister','Menikah',1,90,4100000),
('Dewi Kartika',40,'Diploma','Menikah',2,100,4300000),
('Eko Nugroho',48,'SMA','Menikah',3,140,5600000),
('Farah Anindya',31,'Sarjana','Belum Menikah',0,70,3000000),
('Gilang Ramadhan',38,'Sarjana','Menikah',2,110,4500000),
('Hadi Santoso',55,'SMP','Menikah',4,160,6200000),
('Indah Permata',36,'Sarjana','Menikah',2,95,3800000),
('Joko Susanto',60,'SD','Menikah',3,170,6500000),
('Kurnia Putra',42,'Sarjana','Menikah',2,125,5100000),
('Lestari Ayu',29,'Magister','Belum Menikah',0,75,2900000),
('Maman Suherman',50,'SMA','Menikah',3,150,5800000),
('Nina Oktaviani',33,'Diploma','Menikah',1,85,3600000),
('Omar Dani',44,'Sarjana','Menikah',2,115,4700000),
('Putra Saputra',39,'Sarjana','Menikah',2,105,4400000),
('Rina Wati',37,'Diploma','Menikah',2,95,4000000),
('Slamet Riyadi',53,'SMA','Menikah',4,155,6100000),
('Tari Puspita',30,'Sarjana','Belum Menikah',0,80,3200000),
('Ujang Mulyana',47,'SMP','Menikah',3,145,5400000),
('Vivi Lestari',35,'Sarjana','Menikah',1,90,3700000),
('Wawan Setiawan',46,'SMA','Menikah',3,135,5000000),
('Yuni Astuti',32,'Sarjana','Menikah',1,88,3500000),
('Zainal Abidin',54,'SMA','Menikah',4,160,6400000),
('Adi Pratama',41,'Sarjana','Menikah',2,120,4800000),
('Bayu Firmansyah',36,'Diploma','Menikah',2,100,4200000),
('Cahya Nugraha',38,'Sarjana','Menikah',2,110,4600000),
('Dian Lestari',34,'Magister','Menikah',1,92,3900000),
('Evi Handayani',43,'Diploma','Menikah',3,118,5100000),
('Fikri Ramadhan',28,'Sarjana','Belum Menikah',0,75,3100000),
('Gita Pertiwi',31,'Sarjana','Menikah',1,85,3400000),
('Herman Saputra',49,'SMA','Menikah',3,140,5600000),
('Irwan Kurniawan',45,'Sarjana','Menikah',2,130,5000000),
('Jihan Rahma',27,'Sarjana','Belum Menikah',0,70,2800000),
('Kamaluddin',52,'SMP','Menikah',4,155,6000000),
('Linda Sari',39,'Diploma','Menikah',2,105,4300000),
('Mira Ananda',33,'Sarjana','Menikah',1,90,3600000),
('Naufal Hakim',37,'Sarjana','Menikah',2,112,4500000),
('Oki Setiawan',46,'SMA','Menikah',3,138,5200000),
('Prita Maharani',35,'Sarjana','Menikah',1,95,4000000);

-- ====================================
-- 5. financial_records
-- ====================================
INSERT INTO financial_records
(household_id, main_job, monthly_income, monthly_expense, savings, debt)
VALUES
(1,'Guru',8500000,5200000,2800000,1000000),
(2,'Pengusaha',13000000,4700000,6000000,2000000),
(3,'Akuntan',9500000,4100000,3500000,500000),
(4,'Perawat',9000000,4300000,3000000,800000),
(5,'Sopir',8000000,5600000,1500000,1200000),
(6,'Desainer Grafis',7500000,3000000,3500000,300000),
(7,'Pegawai Bank',10500000,4500000,4500000,900000),
(8,'Petani',9000000,6200000,1500000,2000000),
(9,'Konsultan',14000000,3800000,7500000,600000),
(10,'Pensiunan',6500000,6500000,400000,1200000),
(11,'Pegawai Negeri',11000000,5100000,4500000,700000),
(12,'Freelancer',7000000,2900000,3000000,400000),
(13,'Pedagang',9500000,5800000,2000000,2500000),
(14,'Teknisi',7800000,3600000,2200000,700000),
(15,'Programmer',15000000,4700000,8000000,500000),
(16,'Marketing',9000000,4400000,3500000,800000),
(17,'Admin Kantor',8200000,4000000,2500000,700000),
(18,'Buruh Pabrik',7500000,6100000,900000,1800000),
(19,'Data Analis',15500000,3200000,9000000,300000),
(20,'Manajer Logistik',13000000,5400000,6000000,1500000),
(21,'Guru',8500000,3700000,4000000,600000),
(22,'Montir',7800000,5000000,1800000,900000),
(23,'Programmer',14500000,4600000,7500000,500000),
(24,'Dokter',20000000,6400000,11000000,800000),
(25,'Arsitek',13500000,4800000,6500000,700000),
(26,'Wirausaha',12000000,4200000,5000000,2000000),
(27,'Petani',8800000,4600000,2000000,1500000),
(28,'Dosen',16000000,3900000,9000000,500000),
(29,'Pedagang',9200000,5100000,2200000,2000000),
(30,'Konten Kreator',8000000,3100000,3500000,600000),
(31,'HRD',10000000,3400000,5000000,700000),
(32,'Supir Truk',8500000,5600000,1500000,1800000),
(33,'Konsultan IT',17000000,5000000,9000000,700000),
(34,'Mahasiswa Freelance',6000000,2800000,2500000,200000),
(35,'Peternak',9000000,6000000,1500000,2000000),
(36,'Pegawai Swasta',9500000,4300000,3500000,1000000),
(37,'Apoteker',11000000,3600000,5000000,600000),
(38,'Programmer',15000000,4500000,8500000,500000),
(39,'Pedagang Online',10000000,5200000,3000000,1500000),
(40,'Karyawan Gudang',7800000,4000000,2000000,900000);