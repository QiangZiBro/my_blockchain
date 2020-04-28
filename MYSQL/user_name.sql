# name, real_pass, role, email, address, account, credit
CREATE TABLE IF NOT EXISTS `all_users`
(
    `user_name`      VARCHAR(100) NOT NULL,
    `password` VARCHAR(20)  NOT NULL,
    `role`      VARCHAR(40)  NOT NULL,
    `email`     VARCHAR(40)  ,
    `address`   VARCHAR(40)  ,
    `account`   INTEGER(40)  ,
    `credit`   INTEGER(40),
    `user_port`   INTEGER(40),
    `user_host`   VARCHAR(40)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8;
