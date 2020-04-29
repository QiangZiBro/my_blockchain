# all_goods(goods_id,goods_name,goods_amount,goods_seller,goods_stripeID,
#           goods_price,goods_stat,price_ava
#         ,seller_host,seller_port)
#         values(%d,"%s",%d,"%s","%s","%f","for sale",%f,"%s",%d)
CREATE TABLE IF NOT EXISTS `all_goods`
(
    `goods_id`       INTEGER(20),
    `goods_name`     VARCHAR(20),
    `goods_amount`   VARCHAR(40),
    `goods_seller`   VARCHAR(40),
    `goods_stripeID` VARCHAR(40),
    `good_price`     FLOAT(40),
    `goods_stat`     VARCHAR(40),
    `goods_ava`      FLOAT(40),
    `seller_host`    VARCHAR(40),
    `seller_port`    INTEGER(10)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8;
