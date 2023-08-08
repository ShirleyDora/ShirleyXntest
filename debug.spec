# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['debug.py'],
    pathex=[],
    binaries=[],
    datas=[('./view','view'),('./templates','templates'),('./static','static'),('./report','report'),('./public','public'),('./adblog','adblog')],
    hiddenimports=['solox','solox.public','solox.public.apm','solox.public.apm_pk','solox.public.common'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='岚图性能监控平台',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
	icon='favicon.ico',
	version='file_version_info.txt',
)
