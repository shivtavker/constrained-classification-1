from expt import run_expt

expt_param = {'training_frac': 2.0/3.0, 'num_trials': 5, 'verbosity': True, 'num_ticks': 6}
solver_param = {'eta_list': [0.01,0.1,1,10,100,1000], 'num_inner_iter': 10, 'num_outer_iter': 100}

data = raw_input("dataset (abalone/adult/compas/crimes/default/page-blocks): ")
loss = raw_input("loss function (err/hmean/qmean/fmeasure/microF1): ")
cons = raw_input("constraint function (cov/dp/kld/nae or unconstrained): ")
expt_param['is_protected'] = True if cons == 'dp' else False
if cons == 'unc' or cons == 'unconstrained':
    run_expt(loss, '', data, expt_param, solver_param)
else:
    eps = raw_input("eps: ")
    run_expt(loss, cons, data, expt_param, solver_param, float(eps))

