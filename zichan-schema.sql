-- zichan.sql

drop database if exists asset;

create database asset;

use asset;

grant all privileges on asset.* to 'zichan'@'localhost' identified by 'zichan901';
