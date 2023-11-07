from .builder import _ensure_antlr_files_up_to_date_on_import

_ensure_antlr_files_up_to_date_on_import('McComp', deps=('McCommon', 'cpp'), verbose=True)
_ensure_antlr_files_up_to_date_on_import('McInstr', deps=('McCommon', 'cpp'), verbose=True)
_ensure_antlr_files_up_to_date_on_import('C', verbose=True)
