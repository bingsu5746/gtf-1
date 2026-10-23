"""원작 데이터블록(vanilla/34873)과 우리 모드 데이터블록(mod/SIGNAL)을 읽는 도우미."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VANILLA = ROOT / "vanilla" / "34873"
MOD = ROOT / "mod" / "SIGNAL"


def _path(base, name):
    return base / f"GameData_{name}DataBlock_bin.json"


def load_vanilla(name):
    """예: load_vanilla('Enemy') → 원작 EnemyDataBlock 전체(dict)."""
    with open(_path(VANILLA, name), encoding="utf-8") as f:
        return json.load(f)


def load(name):
    """우리 모드에 파일이 있으면 그걸, 없으면 원작 파일을 읽는다."""
    p = _path(MOD, name)
    if not p.exists():
        p = _path(VANILLA, name)
    with open(p, encoding="utf-8") as f:
        return json.load(f)


def save(name, data):
    """우리 모드 폴더에 데이터블록을 저장한다."""
    MOD.mkdir(parents=True, exist_ok=True)
    with open(_path(MOD, name), "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def block(data, persistent_id):
    return next(b for b in data["Blocks"] if b["persistentID"] == persistent_id)
