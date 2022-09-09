#==============×==============#
#      Created by: Alfa-Ex
#=========× AyiinXd ×=========#

FROM ayiinxd/ayiin-userbot:buster

RUN git clone -b Uputt-Userbot https://github.com/iamuput/Uputt-Userbot /home/uputtuserbot/ \
    && chmod 777 /home/uputtuserbot \
    && mkdir /home/uputtuserbot/bin/

COPY ./sample_config.env ./config.env* /home/
uputuserbot/

WORKDIR /home/uputtuserbot/

RUN pip install -r requirements.txt

CMD ["bash","start"]
