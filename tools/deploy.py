"""mod/SIGNAL 폴더를 r2modman 프로필의 플러그인 폴더로 복사해 게임에 반영한다.

사용법: python tools/deploy.py [프로필 이름]   (기본값: Default)
"""
import os
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "mod" / "SIGNAL"


def main():
    profile = sys.argv[1] if len(sys.argv) > 1 else "Default"
    appdata = os.environ.get("APPDATA")
    if not appdata:
        sys.exit("APPDATA 환경 변수가 없어요. Windows에서 실행해 주세요.")
    profile_dir = Path(appdata) / "r2modmanPlus-local" / "GTFO" / "profiles" / profile
    if not profile_dir.is_dir():
        sys.exit(f"r2modman 프로필을 찾을 수 없어요: {profile_dir}")

    dest = profile_dir / "BepInEx" / "plugins" / "Yeonwoo-SIGNAL" / "SIGNAL"
    if dest.exists():
        shutil.rmtree(dest)
    shutil.copytree(SRC, dest)
    files = sorted(p.name for p in dest.iterdir())
    print(f"{len(files)}개 파일을 반영했어요 → {dest}")
    for name in files:
        print("  " + name)


if __name__ == "__main__":
    main()
