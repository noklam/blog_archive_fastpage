def do_swa()
""" Wrap any optimizer inside SWA wrapper"""
optimizer = SWA(optimizer, swa_start=args.swa_start * steps_per_epoch,
                swa_freq=steps_per_epoch, swa_lr=args.swa_lr)


def do_swa_update():
    """ Always update bn after averaging weight"""
    optimizer.swap_swa_sgd()
    optimizer.bn_update(loaders['train'], model, device='cuda')