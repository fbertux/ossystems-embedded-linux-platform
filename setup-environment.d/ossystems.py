def __after_init_ossystems_yocto():
    PLATFORM_ROOT_DIR = os.environ['PLATFORM_ROOT_DIR']

    append_layers([ os.path.join(PLATFORM_ROOT_DIR, 'sources', p) for p in
                    [
                        'meta-arm/meta-arm',
                        'meta-arm/meta-arm-toolchain',
                        'meta-freescale',
                        'meta-freescale',
                        'meta-freescale-3rdparty',
                        'meta-openembedded/meta-networking',
                        'meta-openembedded/meta-oe',
                        'meta-openembedded/meta-python',
                        'meta-qt5',
                        'meta-raspberrypi',
                        'meta-shellhub',
                        'meta-ti',
                        'meta-webkit',
                    ]])

    # FSL EULA
    eulas.accept['meta-freescale/EULA'] = 'ACCEPT_FSL_EULA = "1"'

run_after_init(__after_init_ossystems_yocto)
