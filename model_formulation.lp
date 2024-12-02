\ Model VRP-CC
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  0 Is_job_1_predecessor_of_job_1? + 4 Is_job_1_predecessor_of_job_2?
   + 500 Is_job_1_predecessor_of_job_3?
   + 300 Is_job_1_predecessor_of_job_4?
   + 100 Is_job_1_predecessor_of_job_5? + 4 Is_job_2_predecessor_of_job_1?
   + 2 Is_job_2_predecessor_of_job_3? + 900 Is_job_2_predecessor_of_job_4?
   + 800 Is_job_2_predecessor_of_job_5?
   + 500 Is_job_3_predecessor_of_job_1? + 2 Is_job_3_predecessor_of_job_2?
   + 3 Is_job_3_predecessor_of_job_4? + 600 Is_job_3_predecessor_of_job_5?
   + 300 Is_job_4_predecessor_of_job_1?
   + 900 Is_job_4_predecessor_of_job_2? + 3 Is_job_4_predecessor_of_job_3?
   + 5 Is_job_4_predecessor_of_job_5? + 800 Is_job_5_predecessor_of_job_2?
   + 600 Is_job_5_predecessor_of_job_3? + 5 Is_job_5_predecessor_of_job_4?
   + 6 Job_2_is_executed_on_day_ + 7 Job_3_is_executed_on_day_
   + 3 Job_4_is_executed_on_day_
Subject To
 (11)_Job_1_only_1_predecessor: Is_job_1_predecessor_of_job_2?
   + Is_job_1_predecessor_of_job_3? + Is_job_1_predecessor_of_job_4?
   + Is_job_1_predecessor_of_job_5? = 1
 (12)_Job_1_only_1_successor: Is_job_2_predecessor_of_job_1?
   + Is_job_3_predecessor_of_job_1? + Is_job_4_predecessor_of_job_1?
   + Is_job_5_predecessor_of_job_1? = 1
 (11)_Job_2_only_1_predecessor: Is_job_2_predecessor_of_job_1?
   + Is_job_2_predecessor_of_job_3? + Is_job_2_predecessor_of_job_4?
   + Is_job_2_predecessor_of_job_5? = 1
 (12)_Job_2_only_1_successor: Is_job_1_predecessor_of_job_2?
   + Is_job_3_predecessor_of_job_2? + Is_job_4_predecessor_of_job_2?
   + Is_job_5_predecessor_of_job_2? = 1
 (11)_Job_3_only_1_predecessor: Is_job_3_predecessor_of_job_1?
   + Is_job_3_predecessor_of_job_2? + Is_job_3_predecessor_of_job_4?
   + Is_job_3_predecessor_of_job_5? = 1
 (12)_Job_3_only_1_successor: Is_job_1_predecessor_of_job_3?
   + Is_job_2_predecessor_of_job_3? + Is_job_4_predecessor_of_job_3?
   + Is_job_5_predecessor_of_job_3? = 1
 (11)_Job_4_only_1_predecessor: Is_job_4_predecessor_of_job_1?
   + Is_job_4_predecessor_of_job_2? + Is_job_4_predecessor_of_job_3?
   + Is_job_4_predecessor_of_job_5? = 1
 (12)_Job_4_only_1_successor: Is_job_1_predecessor_of_job_4?
   + Is_job_2_predecessor_of_job_4? + Is_job_3_predecessor_of_job_4?
   + Is_job_5_predecessor_of_job_4? = 1
 (11)_Job_5_only_1_predecessor: Is_job_5_predecessor_of_job_1?
   + Is_job_5_predecessor_of_job_2? + Is_job_5_predecessor_of_job_3?
   + Is_job_5_predecessor_of_job_4? = 1
 (12)_Job_5_only_1_successor: Is_job_1_predecessor_of_job_5?
   + Is_job_2_predecessor_of_job_5? + Is_job_3_predecessor_of_job_5?
   + Is_job_4_predecessor_of_job_5? = 1
 (13): Is_job_5_predecessor_of_job_1? = 1
 (15)_k=1,_l=1: Is_job_1_predecessor_of_job_5? = 0
 (17)_k=1: Job_1_is_executed_by_machine_ = 1
 (18)_k=1: Job_5_is_executed_by_machine_ = 1
 (19)_i=1,_j=2: Is_job_1_predecessor_of_job_2?
   + Job_1_is_executed_by_machine_ - Job_2_is_executed_by_machine_ <= 1
 (19)_i=1,_j=3: Is_job_1_predecessor_of_job_3?
   + Job_1_is_executed_by_machine_ - Job_3_is_executed_by_machine_ <= 1
 (19)_i=1,_j=4: Is_job_1_predecessor_of_job_4?
   + Job_1_is_executed_by_machine_ - Job_4_is_executed_by_machine_ <= 1
 (19)_i=1,_j=5: Is_job_1_predecessor_of_job_5?
   + Job_1_is_executed_by_machine_ - Job_5_is_executed_by_machine_ <= 1
 (19)_i=2,_j=2: Is_job_2_predecessor_of_job_2? <= 1
 (19)_i=2,_j=3: Is_job_2_predecessor_of_job_3?
   + Job_2_is_executed_by_machine_ - Job_3_is_executed_by_machine_ <= 1
 (19)_i=2,_j=4: Is_job_2_predecessor_of_job_4?
   + Job_2_is_executed_by_machine_ - Job_4_is_executed_by_machine_ <= 1
 (19)_i=2,_j=5: Is_job_2_predecessor_of_job_5?
   + Job_2_is_executed_by_machine_ - Job_5_is_executed_by_machine_ <= 1
 (19)_i=3,_j=2: Is_job_3_predecessor_of_job_2?
   - Job_2_is_executed_by_machine_ + Job_3_is_executed_by_machine_ <= 1
 (19)_i=3,_j=3: Is_job_3_predecessor_of_job_3? <= 1
 (19)_i=3,_j=4: Is_job_3_predecessor_of_job_4?
   + Job_3_is_executed_by_machine_ - Job_4_is_executed_by_machine_ <= 1
 (19)_i=3,_j=5: Is_job_3_predecessor_of_job_5?
   + Job_3_is_executed_by_machine_ - Job_5_is_executed_by_machine_ <= 1
 (19)_i=4,_j=2: Is_job_4_predecessor_of_job_2?
   - Job_2_is_executed_by_machine_ + Job_4_is_executed_by_machine_ <= 1
 (19)_i=4,_j=3: Is_job_4_predecessor_of_job_3?
   - Job_3_is_executed_by_machine_ + Job_4_is_executed_by_machine_ <= 1
 (19)_i=4,_j=4: Is_job_4_predecessor_of_job_4? <= 1
 (19)_i=4,_j=5: Is_job_4_predecessor_of_job_5?
   + Job_4_is_executed_by_machine_ - Job_5_is_executed_by_machine_ <= 1
 (19)_i=5,_j=2: Is_job_5_predecessor_of_job_2?
   - Job_2_is_executed_by_machine_ + Job_5_is_executed_by_machine_ <= 1
 (19)_i=5,_j=3: Is_job_5_predecessor_of_job_3?
   - Job_3_is_executed_by_machine_ + Job_5_is_executed_by_machine_ <= 1
 (19)_i=5,_j=4: Is_job_5_predecessor_of_job_4?
   - Job_4_is_executed_by_machine_ + Job_5_is_executed_by_machine_ <= 1
 (19)_i=5,_j=5: Is_job_5_predecessor_of_job_5? <= 1
 (21_1_start_day)_k=1: Job_1_is_executed_on_day_ = 0
 (21_2_start_minute)_k=1: Job_1_is_executed_on_minute_ = 0
 (22)_i=1,_j=2: 1.0003e+06 Is_job_1_predecessor_of_job_2?
   + 1440 Job_1_is_executed_on_day_ - 1440 Job_2_is_executed_on_day_
   + Job_1_is_executed_on_minute_ - Job_2_is_executed_on_minute_ <= 1e+06
 (22)_i=1,_j=3: 1.05e+06 Is_job_1_predecessor_of_job_3?
   + 1440 Job_1_is_executed_on_day_ - 1440 Job_3_is_executed_on_day_
   + Job_1_is_executed_on_minute_ - Job_3_is_executed_on_minute_ <= 1e+06
 (22)_i=1,_j=4: 1.06e+06 Is_job_1_predecessor_of_job_4?
   + 1440 Job_1_is_executed_on_day_ - 1440 Job_4_is_executed_on_day_
   + Job_1_is_executed_on_minute_ - Job_4_is_executed_on_minute_ <= 1e+06
 (22)_i=1,_j=5: 1.07e+06 Is_job_1_predecessor_of_job_5?
   + 1440 Job_1_is_executed_on_day_ - 1440 Job_5_is_executed_on_day_
   + Job_1_is_executed_on_minute_ - Job_5_is_executed_on_minute_ <= 1e+06
 (22)_i=2,_j=3: 1.00015e+06 Is_job_2_predecessor_of_job_3?
   + 1440 Job_2_is_executed_on_day_ - 1440 Job_3_is_executed_on_day_
   + Job_2_is_executed_on_minute_ - Job_3_is_executed_on_minute_ <= 1e+06
 (22)_i=2,_j=4: 1.0901e+06 Is_job_2_predecessor_of_job_4?
   + 1440 Job_2_is_executed_on_day_ - 1440 Job_4_is_executed_on_day_
   + Job_2_is_executed_on_minute_ - Job_4_is_executed_on_minute_ <= 1e+06
 (22)_i=2,_j=5: 1.0451e+06 Is_job_2_predecessor_of_job_5?
   + 1440 Job_2_is_executed_on_day_ - 1440 Job_5_is_executed_on_day_
   + Job_2_is_executed_on_minute_ - Job_5_is_executed_on_minute_ <= 1e+06
 (22)_i=3,_j=2: 1.00013e+06 Is_job_3_predecessor_of_job_2?
   - 1440 Job_2_is_executed_on_day_ + 1440 Job_3_is_executed_on_day_
   - Job_2_is_executed_on_minute_ + Job_3_is_executed_on_minute_ <= 1e+06
 (22)_i=3,_j=4: 1.00017e+06 Is_job_3_predecessor_of_job_4?
   + 1440 Job_3_is_executed_on_day_ - 1440 Job_4_is_executed_on_day_
   + Job_3_is_executed_on_minute_ - Job_4_is_executed_on_minute_ <= 1e+06
 (22)_i=3,_j=5: 1.05508e+06 Is_job_3_predecessor_of_job_5?
   + 1440 Job_3_is_executed_on_day_ - 1440 Job_5_is_executed_on_day_
   + Job_3_is_executed_on_minute_ - Job_5_is_executed_on_minute_ <= 1e+06
 (22)_i=4,_j=2: 1.09006e+06 Is_job_4_predecessor_of_job_2?
   - 1440 Job_2_is_executed_on_day_ + 1440 Job_4_is_executed_on_day_
   - Job_2_is_executed_on_minute_ + Job_4_is_executed_on_minute_ <= 1e+06
 (22)_i=4,_j=3: 1.00015e+06 Is_job_4_predecessor_of_job_3?
   - 1440 Job_3_is_executed_on_day_ + 1440 Job_4_is_executed_on_day_
   - Job_3_is_executed_on_minute_ + Job_4_is_executed_on_minute_ <= 1e+06
 (22)_i=4,_j=5: 1.00009e+06 Is_job_4_predecessor_of_job_5?
   + 1440 Job_4_is_executed_on_day_ - 1440 Job_5_is_executed_on_day_
   + Job_4_is_executed_on_minute_ - Job_5_is_executed_on_minute_ <= 1e+06
 (22)_i=5,_j=2: 1.045e+06 Is_job_5_predecessor_of_job_2?
   - 1440 Job_2_is_executed_on_day_ + 1440 Job_5_is_executed_on_day_
   - Job_2_is_executed_on_minute_ + Job_5_is_executed_on_minute_ <= 1e+06
 (22)_i=5,_j=3: 1.055e+06 Is_job_5_predecessor_of_job_3?
   - 1440 Job_3_is_executed_on_day_ + 1440 Job_5_is_executed_on_day_
   - Job_3_is_executed_on_minute_ + Job_5_is_executed_on_minute_ <= 1e+06
 (22)_i=5,_j=4: 1.00003e+06 Is_job_5_predecessor_of_job_4?
   - 1440 Job_4_is_executed_on_day_ + 1440 Job_5_is_executed_on_day_
   - Job_4_is_executed_on_minute_ + Job_5_is_executed_on_minute_ <= 1e+06
 (23_1)_i=1: - Job_1_is_executed_on_day_ <= 0
 (23_2)_i=1: Job_1_is_executed_on_day_ <= 100
 (23_1)_i=2: - Job_2_is_executed_on_day_ <= 0
 (23_2)_i=2: Job_2_is_executed_on_day_ <= 100
 (23_1)_i=3: - Job_3_is_executed_on_day_ <= 0
 (23_2)_i=3: Job_3_is_executed_on_day_ <= 100
 (23_1)_i=4: - Job_4_is_executed_on_day_ <= 0
 (23_2)_i=4: Job_4_is_executed_on_day_ <= 100
 (23_1)_i=5: - Job_5_is_executed_on_day_ <= 0
 (23_2)_i=5: Job_5_is_executed_on_day_ <= 100
 (24_1)_i=1: - Job_1_is_executed_on_minute_ <= 0
 (24_2)_i=1: Job_1_is_executed_on_minute_ <= 480
 (24_1)_i=2: - Job_2_is_executed_on_minute_ <= 0
 (24_2)_i=2: Job_2_is_executed_on_minute_ <= 380
 (24_1)_i=3: - Job_3_is_executed_on_minute_ <= 0
 (24_2)_i=3: Job_3_is_executed_on_minute_ <= 400
 (24_1)_i=4: - Job_4_is_executed_on_minute_ <= 0
 (24_2)_i=4: Job_4_is_executed_on_minute_ <= 420
 (24_1)_i=5: - Job_5_is_executed_on_minute_ <= 0
 (24_2)_i=5: Job_5_is_executed_on_minute_ <= 480
Bounds
 Job_1_is_executed_by_machine_ <= 1
 Job_2_is_executed_by_machine_ <= 1
 Job_3_is_executed_by_machine_ <= 1
 Job_4_is_executed_by_machine_ <= 1
 Job_5_is_executed_by_machine_ <= 1
 Job_1_is_executed_on_minute_ <= 480
 Job_2_is_executed_on_minute_ <= 480
 Job_3_is_executed_on_minute_ <= 480
 Job_4_is_executed_on_minute_ <= 480
 Job_5_is_executed_on_minute_ <= 480
Binaries
 Is_job_1_predecessor_of_job_1? Is_job_1_predecessor_of_job_2?
 Is_job_1_predecessor_of_job_3? Is_job_1_predecessor_of_job_4?
 Is_job_1_predecessor_of_job_5? Is_job_2_predecessor_of_job_1?
 Is_job_2_predecessor_of_job_2? Is_job_2_predecessor_of_job_3?
 Is_job_2_predecessor_of_job_4? Is_job_2_predecessor_of_job_5?
 Is_job_3_predecessor_of_job_1? Is_job_3_predecessor_of_job_2?
 Is_job_3_predecessor_of_job_3? Is_job_3_predecessor_of_job_4?
 Is_job_3_predecessor_of_job_5? Is_job_4_predecessor_of_job_1?
 Is_job_4_predecessor_of_job_2? Is_job_4_predecessor_of_job_3?
 Is_job_4_predecessor_of_job_4? Is_job_4_predecessor_of_job_5?
 Is_job_5_predecessor_of_job_1? Is_job_5_predecessor_of_job_2?
 Is_job_5_predecessor_of_job_3? Is_job_5_predecessor_of_job_4?
 Is_job_5_predecessor_of_job_5?
Generals
 Job_1_is_executed_by_machine_ Job_2_is_executed_by_machine_
 Job_3_is_executed_by_machine_ Job_4_is_executed_by_machine_
 Job_5_is_executed_by_machine_ Job_1_is_executed_on_day_
 Job_2_is_executed_on_day_ Job_3_is_executed_on_day_
 Job_4_is_executed_on_day_ Job_5_is_executed_on_day_
 Job_1_is_executed_on_minute_ Job_2_is_executed_on_minute_
 Job_3_is_executed_on_minute_ Job_4_is_executed_on_minute_
 Job_5_is_executed_on_minute_
End
