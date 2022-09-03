#==============×==============#
#      Created by: Alfa-Ex
#=========× AyiinXd ×=========#

FROM ayiinxd/ayiin-userbot:buster

RUN git clone -b Uputt-Userbot https://github.com/iamuput/Uputt-Userbot /home/uputtuserbot/ \
    && chmod 777 /home/nandetelethon \
    && mkdir /home/nandetelethon/bin/

COPY ./sample_config.env ./config.env* /home/nandetelethon/

WORKDIR /home/uputtuserbot/

RUN pip install -r requirements.txt

CMD ["bash","start"]
