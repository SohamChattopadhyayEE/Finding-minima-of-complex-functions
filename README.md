#  Gravitational Search Algorithm
Python Code for Gravitational Search Algorithm (GSA) for minimization of 20 different benchmark functions. The code is compatable to python 2.* or 3.* versions.

## Reference
[Rashedi, Esmat, Hossein Nezamabadi-Pour, and Saeid Saryazdi. "GSA: a gravitational search algorithm." 
Information sciences 179.13 (2009): 2232-2248.](https://www.sciencedirect.com/science/article/abs/pii/S0020025509001200)	

## Dependencies
    pip install requirements.text

## Implementation
- ### Arguments 
        E:\.\directory> python optimizer.py --help
        usage: optimizer.py [-h] [-is_GSA] [-is_sf] [-is_bcf] [-is_rhe] [-is_df] [-is_zf] [-is_lf] [-is_ef] [-is_s12f] [-is_s22f] [-is_rf]
                            [-is_s226f] [-is_stf] [-is_sf2f] [-is_sf6f] [-is_bf] [-is_rbf] [-is_gf] [-is_tf] [-is_hf3] [-is_hf1] [-is_exp]
                            [-p POP_SIZE] [-i ITER] [-r RUN]

        Minimization of 20 benchmark functions

        optional arguments:
          -h, --help            show this help message and exit
          -is_GSA, --GSA        If GSA is to be used
          -is_sf, --sphere_function
                                Sphere function
          -is_bcf, --bent_cigar_function
                                Bent Cigar function
          -is_rhe, --RHE_function
                                Rotated Hyper-ellipsoid (RHE) function
          -is_df, --discus_function
                                Discus function
          -is_zf, --zettl_function
                                Zettl function
          -is_lf, --leon_function
                                Leon function
          -is_ef, --easom_function
                                Easom function
          -is_s12f, --schwefel_12_function
                                Schwefel 1.2 function
          -is_s22f, --schwefel_22_function
                                Schwefel 2.2 function
          -is_rf, --rastrigin_function
                                Rastrigin function
          -is_s226f, --schwefel_226_function
                                Schwefel 22.6 function
          -is_stf, --st_function
                                Styblinski-Tang (ST) function
          -is_sf2f, --schaffer_f2_function
                                Schaffer F2 function
          -is_sf6f, --schaffer_f6_function
                                Schaffer F6 function
          -is_bf, --bird_function
                                Bird function
          -is_rbf, --rosenbrock_function
                                Rosenbrock function
          -is_gf, --griewank_function
                                Griewank function
          -is_tf, --trigonometric_function
                                Trigonometric function
          -is_hf3, --hf3        Hybrid function – 3
          -is_hf1, --hf1        Hybrid function – 1
          -is_exp, --export     Whether output .csv to be exported
          -p POP_SIZE, --pop_size POP_SIZE
                                Population size
          -i ITER, --iter ITER  Number of iterations
          -r RUN, --run RUN     Number of runs
- 20 fitness functions are used for evaluation of GSA algorithm. 
