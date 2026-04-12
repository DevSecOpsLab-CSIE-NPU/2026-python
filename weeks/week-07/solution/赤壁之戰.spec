# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['正式遊戲版本.py'],
    pathex=[],
    binaries=[],
    datas=[('../generals.txt', '.'), ('../battles.txt', '.'), ('遊戲圖片', '遊戲圖片')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='赤壁之戰',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='赤壁之戰',
)
app = BUNDLE(
    coll,
    name='赤壁之戰.app',
    icon='遊戲圖片/赤壁之戰.icns',
    bundle_identifier=None,
)
