Set-Location -LiteralPath "$PSScriptRoot\01_resources\repos"
$repos = @(
  @{Name="islp_labs"; Url="https://github.com/intro-stat-learning/ISLP_labs.git"},
  @{Name="handson-ml3"; Url="https://github.com/ageron/handson-ml3.git"},
  @{Name="scikit-learn-mooc"; Url="https://github.com/INRIA/scikit-learn-mooc.git"},
  @{Name="ml-from-scratch"; Url="https://github.com/eriklindernoren/ML-From-Scratch.git"},
  @{Name="raschka-machine-learning-book"; Url="https://github.com/rasbt/machine-learning-book.git"},
  @{Name="d2l-en"; Url="https://github.com/d2l-ai/d2l-en.git"},
  @{Name="pytorch-tutorials"; Url="https://github.com/pytorch/tutorials.git"},
  @{Name="pytorch-examples"; Url="https://github.com/pytorch/examples.git"},
  @{Name="fastbook"; Url="https://github.com/fastai/fastbook.git"},
  @{Name="micrograd"; Url="https://github.com/karpathy/micrograd.git"},
  @{Name="makemore"; Url="https://github.com/karpathy/makemore.git"},
  @{Name="nanochat"; Url="https://github.com/karpathy/nanochat.git"},
  @{Name="nanoGPT_historical"; Url="https://github.com/karpathy/nanoGPT.git"},
  @{Name="huggingface-course"; Url="https://github.com/huggingface/course.git"},
  @{Name="huggingface-notebooks"; Url="https://github.com/huggingface/notebooks.git"},
  @{Name="spinningup"; Url="https://github.com/openai/spinningup.git"},
  @{Name="cleanrl"; Url="https://github.com/vwxyzjn/cleanrl.git"},
  @{Name="made-with-ml"; Url="https://github.com/GokuMohandas/Made-With-ML.git"},
  @{Name="probml-book"; Url="https://github.com/probml/pml-book.git"},
  @{Name="ML-foundations"; Url="https://github.com/jonkrohn/ML-foundations.git"}
)
foreach ($repo in $repos) {
  if (-not (Test-Path -LiteralPath $repo.Name)) {
    git clone --depth 1 $repo.Url $repo.Name
  }
}