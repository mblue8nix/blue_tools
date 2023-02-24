# blue tools 

Tools I created to work on a mac/linux systems that will help in productivity, testing and so on. 

Fake data generator: 

## fkdata-generator
(Generate fake data as files in `json, csv or parquet` format)

- fkdata-generator

```bash
python3 fkdata_generator --file ../data/fkuser_data --records 10000 --format parquet

Generating Fake Data with '10000' records.... 

100%|█████████████████████████████████████████████████████████████████████████████| 10000/10000 [00:18<00:00, 551.32it/s]

Sample Data:
                          Email_Id   Name    Gamer_Id                                     Device        Phone_Number                                                 Address              City Year     Time                     Link  Purchase_Amount
Erin.Brown@montgomery-nichols.com   Erin   Brown6307  iPhone; CPU iPhone OS 9_3_5 like Mac OS X   (009)211-6735x508        48402 Kelly Port Apt. 431\nNorth Brian, PR 81662         Lucasland 2012 06:12:59   https://www.perez.com/              544
       Dennis.King@avila-odom.com Dennis    King3027 iPhone; CPU iPhone OS 14_2_1 like Mac OS X (852)065-5680x15345 92220 Denise Ways Apt. 843\nNorth Sierrashire, WV 39014 East Timothyshire 1976 20:42:58      https://ortega.com/               97
       Tammy.Andrews@garrison.com  Tammy Andrews8289  iPhone; CPU iPhone OS 6_1_6 like Mac OS X    001-319-013-0740      6603 Justin Prairie Apt. 652\nMorrisbury, ID 31143      Nicholeville 1987 07:41:59 http://www.anderson.org/              312 


Created file: ../data/fkuser_data.parquet
With 10000 records of data

```

------------

## Pomodre Clock 
Pom Clock: 
(Simple Pomodoro Clock for time managment.)

After 25 minutes on a task a website will pop for a break. 
You can change the site url by changing the `BREAK_SITE` var. 

- pom-clock 

Usage:
```
pom-clock
```

![pom-clock](https://github.com/mblue8nix/blue_tools/blob/main/pom-im.png)
