# -*- mode: python -*-

block_cipher = None


a = Analysis(['C:\\Users\\usuario\\Desktop\\reportes-neurociencias\\src\\main\\python\\MasterController.py'],
             pathex=['C:\\Users\\usuario\\Desktop\\reportes-neurociencias\\target\\PyInstaller'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=['c:\\users\\usuario\\desktop\\reportes-neurociencias\\venv\\lib\\site-packages\\fbs\\freeze\\hooks'],
             runtime_hooks=['C:\\Users\\usuario\\Desktop\\reportes-neurociencias\\target\\PyInstaller\\fbs_pyinstaller_hook.py'],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='reporte_neurociencias',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          console=True , icon='C:\\Users\\usuario\\Desktop\\reportes-neurociencias\\src\\main\\icons\\Icon.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               name='reporte_neurociencias')