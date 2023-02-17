# blue tools 

Tools repo for my testing and so on. 

- fkdata-generator.py

```bash
sh-3.2$ python3 data_fgenerator --file ../data/user_fake_data --records 100000 --format parquet

Creating file ../data/user_fake_data.parquet with '100000' rows: 

100%|█████████████████████████████████████████████████████████████████████████████████████| 14285/14285 [00:48<00:00, 292.71it/s]

Sample Data:
                       Email_Id          Name Game_Id                                    Device     Phone_Number                                                  Address            City Year     Time                           Link Money_Spent
          Luis.Collier@lee.net  Luis Collier     493 iPhone; CPU iPhone OS 6_1_6 like Mac OS X     317-990-2633 108 Christopher Ford Suite 997\nNew Bradleyton, LA 12542 Lake Melodybury 1982 13:47:19 https://collins-patterson.org/         532
Randy.Carson@mooney-chaney.com  Randy Carson    9265     iPad; CPU iPad OS 5_1_1 like Mac OS X 561.411.0622x459                    5290 Bradley Keys\nShawtown, AL 85423       Reyesland 2018 05:33:15      https://weiss-campos.com/         589
      Steve.Marquez@jordan.com Steve Marquez    9589 iPhone; CPU iPhone OS 5_1_1 like Mac OS X 875-534-8545x647            58752 Johnson Ridges\nSouth Cynthia, NY 51606    New Jennifer 1990 14:28:25          https://www.holt.com/         187 


Created file: ../data/user_fake_data.parquet
With 100000 rows

```
