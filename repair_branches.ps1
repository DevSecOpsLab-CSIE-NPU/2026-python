$STUDENT_ID = "1112405041-李易宸"
$BASE_COMMIT = "a4eadf9"
$BACKUP_BASE = "D:\20260514python\2026-python"

for ($i = 2; $i -le 10; $i++) {
    $WEEK = $i.ToString("00")
    $BRANCH = "week-$WEEK"

    Write-Host "========================================"
    Write-Host "🧹 正在處理 Week $WEEK 的分支..."

    # 重設分支
    git checkout -B $BRANCH $BASE_COMMIT

    # 複製檔案
    $SOURCE = Join-Path $BACKUP_BASE "weeks\week-$WEEK\solutions\1112405041\*"
    $DEST = "weeks/week-$WEEK/solutions/1112405041"

    # 確保目的地存在
    if (!(Test-Path $DEST)) {
        New-Item -ItemType Directory -Path $DEST -Force
    }

    Copy-Item -Path $SOURCE -Destination $DEST -Recurse -Force

    # 提交變更
    git add $DEST
    git commit -m "[Week $WEEK] $STUDENT_ID Submission"

    # 貼上標籤
    $TAGS = @()
    switch ($WEEK) {
        "02" { $TAGS = @("0312") }
        "03" { $TAGS = @("0318", "0319") }
        "04" { $TAGS = @("0325", "0326") }
        "05" { $TAGS = @("0408", "0409") }
        "06" { $TAGS = @("0415", "0416") }
        "07" { $TAGS = @("0422", "0423") }
        "08" { $TAGS = @("0429", "0430") }
        "09" { $TAGS = @("0513", "0514") }
        "10" { $TAGS = @("0520", "0521") }
    }

    foreach ($DATE in $TAGS) {
        $TAG_NAME = "$DATE-$STUDENT_ID"
        git tag -f $TAG_NAME
    }
}

# 回到 main
git checkout main
Write-Host "✅ 所有本地分支修復完成！"
