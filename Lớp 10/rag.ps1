$ErrorActionPreference = 'Stop'
$pythonRuntime = 'D:\Anaconda\envs\taode\python.exe'
if (-not (Test-Path -LiteralPath $pythonRuntime)) {
    throw 'Không thấy môi trường taode. Chạy scripts/index_tai_lieu.py bằng Python có PyMuPDF và OCR vie+eng.'
}
& $pythonRuntime -B -u (Join-Path $PSScriptRoot 'scripts\index_tai_lieu.py') @args
if ($LASTEXITCODE -ne 0) { throw "Local RAG thất bại (mã $LASTEXITCODE). Xem lỗi phía trên." }
