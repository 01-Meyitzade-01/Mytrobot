.. raw:: html

  <img src="https://i.imgur.com/RtXS5Yo.png" width="150" align="right">

MytRobot
=========

|License| |Codacy| |Crowdin| |Black| |Telegram Channel| |Telegram Chat|

Pyrogram ve asenkron programlama ile yapılmış çok amaçlı bir Telegram Botu.

Gereksinimler
------------
- Python 3.6+
- Unix benzeri bir işletim sistemi (Windows'ta çalıştırma %100 desteklenmez. Windows'ta herhangi bir sorun bulursanız, lütfen bir sorun bildirin.)

Kurulum
-------
1. Bir sanal ortam oluşturun (Bu adım isteğe bağlıdır, ancak bağımlılık çakışmalarını önlemek için **kesinlikle** önerilir)

   - ``python3 -m venv .venv`` (tekrar çalıştırmanıza gerek yok)
   - ``. .venv/bin/activate`` (Projeyi her yeni kabukta açtığınızda bunu çalıştırmalısınız.)

2. Gerekli modülleri gereksinimler.txt dosyasından yükleyin. ``pip3 install -Ur requirements.txt``.
3. https://my.telegram.org/apps adresine gidin ve yeni bir uygulama oluşturun.
4. ``config.py.example`` dosyasından (``cp eduu/config.py.example eduu/config.py``) yeni bir ``config.py`` dosyası oluşturun).
5. Simgenizi, kimliklerinizi ve API anahtarlarınızı config.py dosyanıza yerleştirin.


Çalıştırmak
-----------
- Botu çalıştırmak için ``python3 -m eduu`` komutunu çalıştırmanız yeterlidir. Virtualenv'den yüklediyseniz, `` çalıştırın. .venv/bin/activate`` bundan önce.
- tutmak istiyorsanız, `ekranda <https://en.wikipedia.org/wiki/GNU_Screen>`__ veya `tmux <https://en.wikipedia.org/wiki/Tmux>`__ üzerinde çalıştırmanız şiddetle tavsiye edilir. bir sunucuda çalışan bot.

..  [Deploy] https://heroku.com/deploy?template=https://github.com/01-Meyitzade-01/Mytrobot

Not
----
Botla ilgili herhangi bir hata/sorun bulursanız, üç seçeneğiniz vardır.:

- Sorunu açıklayan `GitHub <https://github.com/01-Meyitzade-01/MytRobot>`__ sayfamızda yeni bir sorun oluşturun.
- Sorunu açıklayan `bot'un <https://t.me/MytProGuardBot>`__ sohbetine /bug komutunu gönderin.
- Sorunu nasıl çözeceğinizi biliyorsanız, depomuzu çatallayın ve bir çekme isteği açın.

.. Badges
.. |Black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
.. |Codacy| image:: https://app.codacy.com/project/badge/Grade/7e9bffc2c3a140cf9f1e5d3c4aea0c2f
   :target: https://www.codacy.com/gh/AmanoTeam/EduuRobot/dashboard
.. |Crowdin| image:: https://badges.crowdin.net/eduurobot/localized.svg
   :target: https://crowdin.com/project/eduurobot
.. |License| image:: https://img.shields.io/github/license/AmanoTeam/EduuRobot
.. |Telegram Channel| image:: https://img.shields.io/badge/Telegram-Channel-33A8E3
   :target: https://t.me/Hiraset
.. |Telegram Chat| image:: https://img.shields.io/badge/Telegram-Chat-33A8E3
   :target: https://t.me/HirasetTR
