{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/lee000921/Note/blob/master/pytorch101.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "QcJK3kXl--c3"
      },
      "source": [
        "# EECS 498-007/598-005 Assignment 1-1: PyTorch 101\n",
        "\n",
        "Before we start, please put your name and UMID in following format\n",
        "\n",
        ": Firstname LASTNAME, #00000000   //   e.g.) Justin JOHNSON, #12345678"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "7sA2iBcm_cPb"
      },
      "source": [
        "**Your Answer:**   \n",
        "Your NAME, #XXXXXXXX"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "kQndOAmiVTO3"
      },
      "source": [
        "# Setup Code\n",
        "Before getting started we need to run some boilerplate code to set up our environment. You'll need to rerun this setup code each time you start the notebook.\n",
        "\n",
        "First, run this cell load the [autoreload](https://ipython.readthedocs.io/en/stable/config/extensions/autoreload.html?highlight=autoreload) extension. This allows us to edit `.py` source files, and re-import them into the notebook for a seamless editing and debugging experience."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "H5PzjwH7VTO4"
      },
      "outputs": [],
      "source": [
        "%load_ext autoreload\n",
        "%autoreload 2"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "bCtoiSyVVTO8"
      },
      "source": [
        "### Google Colab Setup\n",
        "Next we need to run a few commands to set up our environment on Google Colab. If you are running this notebook on a local machine you can skip this section.\n",
        "\n",
        "Run the following cell to mount your Google Drive. Follow the link, sign in to your Google account (the same account you used to store this notebook!) and copy the authorization code into the text box that appears below."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "tHG0slB6VTO8"
      },
      "outputs": [],
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/drive')"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "UWjXo-vXVTO_"
      },
      "source": [
        "Now recall the path in your Google Drive where you uploaded this notebook, fill it in below. If everything is working correctly then running the folowing cell should print the filenames from the assignment:\n",
        "\n",
        "```\n",
        "['pytorch101.py', 'knn.py', 'knn.ipynb', 'eecs598', 'pytorch101.ipynb']\n",
        "```"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "KqMvJnNHVTPA"
      },
      "outputs": [],
      "source": [
        "import os\n",
        "\n",
        "# TODO: Fill in the Google Drive path where you uploaded the assignment\n",
        "# Example: If you create a 2020FA folder and put all the files under A1 folder, then '2020FA/A1'\n",
        "# GOOGLE_DRIVE_PATH_AFTER_MYDRIVE = '2020FA/A1'\n",
        "GOOGLE_DRIVE_PATH_AFTER_MYDRIVE = None\n",
        "GOOGLE_DRIVE_PATH = os.path.join('drive', 'My Drive', GOOGLE_DRIVE_PATH_AFTER_MYDRIVE)\n",
        "print(os.listdir(GOOGLE_DRIVE_PATH))"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "ko-wLqHWVTPC"
      },
      "source": [
        "Once you have successfully mounted your Google Drive and located the path to this assignment, run the following cell to allow us to import from the `.py` files of this assignment. If it works correctly, it should print the message:\n",
        "\n",
        "```\n",
        "Hello from pytorch101.py!\n",
        "```\n",
        "\n",
        "as well as the last edit time for the file `pytorch101.py`."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "1AoThF9eVTPD"
      },
      "outputs": [],
      "source": [
        "import sys\n",
        "sys.path.append(GOOGLE_DRIVE_PATH)\n",
        "\n",
        "import time, os\n",
        "os.environ[\"TZ\"] = \"US/Eastern\"\n",
        "time.tzset()\n",
        "\n",
        "from pytorch101 import hello\n",
        "hello()\n",
        "\n",
        "pytorch101_path = os.path.join(GOOGLE_DRIVE_PATH, 'pytorch101.py')\n",
        "pytorch101_edit_time = time.ctime(os.path.getmtime(pytorch101_path))\n",
        "print('pytorch101.py last edited on %s' % pytorch101_edit_time)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Qc83ETI1a3o9"
      },
      "source": [
        "# Introduction\n",
        "\n",
        "Python 3 and [PyTorch](https://pytorch.org/) will be used throughout the semseter, so it is important to be familiar with them. This material in this notebook draws from the [Stanford CS231n](http://cs231n.github.io/python-numpy-tutorial/) and [CS228](https://github.com/kuleshov/cs228-material/blob/master/tutorials/python/cs228-python-tutorial.ipynb) Python and numpy tutorials, but this material focuses mainly on PyTorch.\n",
        "\n",
        "This notebook will walk you through many of the important features of PyTorch that you will need to use throughout the semester. In some cells and files you will see code blocks that look like this:\n",
        "\n",
        "```python\n",
        "##############################################################################\n",
        "#                    TODO: Write the equation for a line                     #\n",
        "##############################################################################\n",
        "pass\n",
        "##############################################################################\n",
        "#                              END OF YOUR CODE                              #\n",
        "##############################################################################\n",
        "```\n",
        "\n",
        "You should replace the `pass` statement with your own code and leave the blocks intact, like this:\n",
        "\n",
        "```python\n",
        "##############################################################################\n",
        "#                    TODO: Write the equation for a line                     #\n",
        "##############################################################################\n",
        "y = m * x + b\n",
        "##############################################################################\n",
        "#                              END OF YOUR CODE                              #\n",
        "##############################################################################\n",
        "```\n",
        "\n",
        "When completing the notebook, please adhere to the following rules:\n",
        "- Do not write or modify any code outside of code blocks\n",
        "- Do not add or delete any cells from the notebook. You may add new cells to perform scatch work, but delete them before submitting.\n",
        "- Run all cells before submitting. **You will only get credit for code that has been run!**.\n",
        "\n",
        "The last point is extremely important and bears repeating:\n",
        "\n",
        "### We will not re-run your notebook -- you will only get credit for cells that have been run\n",
        "\n",
        "This notebook contains many inline sanity checks for the code you write. However, **passing these sanity checks does not mean your code is correct!** During grading we may run your code on additional inputs, and we may look at your code to make sure you've followed the specific guildelines for each implementation. You are encouraged to write additional test cases for the functions you are asked to write instead of solely relying on the sanity checks in the notebook."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "hQrEwOpXb9Gh"
      },
      "source": [
        "# Python 3\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "xAKwfCs_mK3d"
      },
      "source": [
        "If you're unfamiliar with Python 3, here are some of the most common changes from Python 2 to look out for.\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "zjosrOn8mOMV"
      },
      "source": [
        "### Print is a function"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "O41SjFuamR7d"
      },
      "outputs": [],
      "source": [
        "print(\"Hello!\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "nEh1swLBmQN-"
      },
      "source": [
        "Without parentheses, printing will not work."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "OgPaSNS2mVPn"
      },
      "source": [
        "### Floating point division by default"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "SQKlRZ8KmYDl"
      },
      "outputs": [],
      "source": [
        "5 / 2"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "DOmfK0WWmb2V"
      },
      "source": [
        "To do integer division, we use two backslashes:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "UUg1MjiPmgNX"
      },
      "outputs": [],
      "source": [
        "5 // 2"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "zeH5501nmh7W"
      },
      "source": [
        "### No xrange"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "3wNKyyilmkMy"
      },
      "source": [
        "The xrange from Python 2 is now merged into \"range\" for Python 3 and there is no xrange in Python 3. In Python 3, range(3) does not create a list of 3 elements as it would in Python 2, rather just creates a more memory efficient iterator.\n",
        "\n",
        "Hence,  \n",
        "xrange in Python 3: Does not exist  \n",
        "range in Python 3: Has very similar behavior to Python 2's xrange"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "dP8Dk9PAmnQh"
      },
      "outputs": [],
      "source": [
        "for i in range(3):\n",
        "    print(i)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "6SKbKDgLmqd-"
      },
      "outputs": [],
      "source": [
        "range(3)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "Wm_VcW3VmsSD"
      },
      "outputs": [],
      "source": [
        "# If need be, can use the following to get a similar behavior to Python 2's range:\n",
        "print(list(range(3)))"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "1MEmHrgBsgX4"
      },
      "source": [
        "# PyTorch"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "c3e_Nux0siHo"
      },
      "source": [
        "[PyTorch](https://pytorch.org/) is an open source machine learning framework. At its core, PyTorch provides a few key features:\n",
        "\n",
        "- A multidimensional **Tensor** object, similar to [numpy](https://numpy.org/) but with GPU accelleration.\n",
        "- An optimized **autograd** engine for automatically computing derivatives\n",
        "- A clean, modular API for building and deploying **deep learning models**\n",
        "\n",
        "We will use PyTorch for all programming assignments throughout the semester. This notebook will focus on the **Tensor API**, as it is the main part of PyTorch that we will use for the first few assignments.\n",
        "\n",
        "You can find more information about PyTorch by following one of the [oficial tutorials](https://pytorch.org/tutorials/) or by [reading the documentation](https://pytorch.org/docs/stable/)."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "zdiO3_y-vKQ9"
      },
      "source": [
        "To use PyTorch, we first need to import the `torch` package.\n",
        "\n",
        "We also check the version; the assignments in this course will use PyTorch verion 1.10.0, since this is the default version in Google Colab."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "sydFm14itrqq"
      },
      "outputs": [],
      "source": [
        "import torch\n",
        "print(torch.__version__)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "HrBSx6hYu8ca"
      },
      "source": [
        "## Tensor Basics"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "LWagwmXuvIle"
      },
      "source": [
        "### Creating and Accessing tensors"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Bf_SY4RzvAh_"
      },
      "source": [
        "A `torch` **tensor** is a multidimensional grid of values, all of the same type, and is indexed by a tuple of nonnegative integers. The number of dimensions is the **rank** of the tensor; the **shape** of a tensor is a tuple of integers giving the size of the array along each dimension.\n",
        "\n",
        "We can initialize `torch` tensor from nested Python lists. We can access or mutate elements of a PyTorch tensor using square brackets.\n",
        "\n",
        "Accessing an element from a PyTorch tensor returns a PyTorch scalar; we can convert this to a Python scalar using the `.item()` method:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "IpwfVUvPu_lF"
      },
      "outputs": [],
      "source": [
        "# Create a rank 1 tensor from a Python list\n",
        "a = torch.tensor([1, 2, 3])\n",
        "print('Here is a:')\n",
        "print(a)\n",
        "print('type(a): ', type(a))\n",
        "print('rank of a: ', a.dim())\n",
        "print('a.shape: ', a.shape)\n",
        "\n",
        "# Access elements using square brackets\n",
        "print()\n",
        "print('a[0]: ', a[0])\n",
        "print('type(a[0]): ', type(a[0]))\n",
        "print('type(a[0].item()): ', type(a[0].item()))\n",
        "\n",
        "# Mutate elements using square brackets\n",
        "a[1] = 10\n",
        "print()\n",
        "print('a after mutating:')\n",
        "print(a)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "FZq4zsnLEgXH"
      },
      "source": [
        "The example above shows a one-dimensional tensor; we can similarly create tensors with two or more dimensions:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "7TcvHxpTFUcL"
      },
      "outputs": [],
      "source": [
        "# Create a two-dimensional tensor\n",
        "b = torch.tensor([[1, 2, 3], [4, 5, 5]])\n",
        "print('Here is b:')\n",
        "print(b)\n",
        "print('rank of b:', b.dim())\n",
        "print('b.shape: ', b.shape)\n",
        "\n",
        "# Access elements from a multidimensional tensor\n",
        "print()\n",
        "print('b[0, 1]:', b[0, 1])\n",
        "print('b[1, 2]:', b[1, 2])\n",
        "\n",
        "# Mutate elements of a multidimensional tensor\n",
        "b[1, 1] = 100\n",
        "print()\n",
        "print('b after mutating:')\n",
        "print(b)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "BBOsvh53GXa8"
      },
      "source": [
        "Now it's **your turn**. In the file `pytorch101.py`, complete the implementation of the functions `create_sample_tensor`, `mutate_tensor`, and `count_tensor_elements` to practice constructing, mutating, and thinking about the shapes of tensors."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "zjCIUzbaVTPs"
      },
      "outputs": [],
      "source": [
        "from pytorch101 import create_sample_tensor, mutate_tensor, count_tensor_elements\n",
        "\n",
        "# Create a sample tensor\n",
        "x = create_sample_tensor()\n",
        "print('Here is the sample tensor:')\n",
        "print(x)\n",
        "\n",
        "# Mutate the tensor by setting a few elements\n",
        "indices = [(0, 0), (1, 0), (1, 1)]\n",
        "values = [4, 5, 6]\n",
        "mutate_tensor(x, indices, values)\n",
        "print('\\nAfter mutating:')\n",
        "print(x)\n",
        "print('\\nCorrect shape: ', x.shape == (3, 2))\n",
        "print('x[0, 0] correct: ', x[0, 0].item() == 4)\n",
        "print('x[1, 0] correct: ', x[1, 0].item() == 5)\n",
        "print('x[1, 1] correct: ', x[1, 1].item() == 6)\n",
        "\n",
        "# Check the number of elements in the sample tensor\n",
        "num = count_tensor_elements(x)\n",
        "print('\\nNumber of elements in x: ', num)\n",
        "print('Correctly counted: ', num == 6)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Yz_VDA3IvP33"
      },
      "source": [
        "### Tensor constructors"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "BoAlslEdwV-k"
      },
      "source": [
        "PyTorch provides many convenience methods for constructing tensors; this avoids the need to use Python lists, which can be inefficient when manipulating large amounts of data. Some of the most commonly used tensor constructors are:\n",
        "\n",
        "- [`torch.zeros`](https://pytorch.org/docs/stable/generated/torch.zeros.html): Creates a tensor of all zeros\n",
        "- [`torch.ones`](https://pytorch.org/docs/stable/generated/torch.ones.html): Creates a tensor of all ones\n",
        "- [`torch.rand`](https://pytorch.org/docs/stable/generated/torch.rand.html): Creates a tensor with uniform random numbers\n",
        "\n",
        "You can find a full list of tensor creation operations [in the documentation](https://pytorch.org/docs/stable/torch.html#creation-ops)."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "FL6DXGXzxHBA"
      },
      "outputs": [],
      "source": [
        "# Create a tensor of all zeros\n",
        "a = torch.zeros(2, 3)\n",
        "print('tensor of zeros:')\n",
        "print(a)\n",
        "\n",
        "# Create a tensor of all ones\n",
        "b = torch.ones(1, 2)\n",
        "print('\\ntensor of ones:')\n",
        "print(b)\n",
        "\n",
        "# Create a 3x3 identity matrix\n",
        "c = torch.eye(3)\n",
        "print('\\nidentity matrix:')\n",
        "print(c)\n",
        "\n",
        "# Tensor of random values\n",
        "d = torch.rand(4, 5)\n",
        "print('\\nrandom tensor:')\n",
        "print(d)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "y9QuvWYxMsoK"
      },
      "source": [
        "**Your turn**: In the file `pytorch101.py`, complete the implementation of `create_tensor_of_pi` to practice using a tensor constructor.\n",
        "\n",
        "Hint: [`torch.full`](https://pytorch.org/docs/stable/generated/torch.full.html#torch.full)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "N_y7Z5I0NIaA"
      },
      "outputs": [],
      "source": [
        "from pytorch101 import create_tensor_of_pi\n",
        "\n",
        "x = create_tensor_of_pi(4, 5)\n",
        "\n",
        "print('x is a tensor:', torch.is_tensor(x))\n",
        "print('x has correct shape: ', x.shape == (4, 5))\n",
        "print('x is filled with pi: ', (x == 3.14).all().item() == 1)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Rz_hiJD33fu1"
      },
      "source": [
        "### Datatypes"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "GG1xBunZ3ixx"
      },
      "source": [
        "In the examples above, you may have noticed that some of our tensors contained floating-point values, while others contained integer values.\n",
        "\n",
        "PyTorch provides a [large set of numeric datatypes](https://pytorch.org/docs/stable/tensor_attributes.html#torch.torch.dtype) that you can use to construct tensors. PyTorch tries to guess a datatype when you create a tensor; functions that construct tensors typically have a `dtype` argument that you can use to explicitly specify a datatype.\n",
        "\n",
        "Each tensor has a `dtype` attribute that you can use to check its data type:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "vREVDf_n31Qz"
      },
      "outputs": [],
      "source": [
        "# Let torch choose the datatype\n",
        "x0 = torch.tensor([1, 2])   # List of integers\n",
        "x1 = torch.tensor([1., 2.]) # List of floats\n",
        "x2 = torch.tensor([1., 2])  # Mixed list\n",
        "print('dtype when torch chooses for us:')\n",
        "print('List of integers:', x0.dtype)\n",
        "print('List of floats:', x1.dtype)\n",
        "print('Mixed list:', x2.dtype)\n",
        "\n",
        "# Force a particular datatype\n",
        "y0 = torch.tensor([1, 2], dtype=torch.float32)  # 32-bit float\n",
        "y1 = torch.tensor([1, 2], dtype=torch.int32)    # 32-bit (signed) integer\n",
        "y2 = torch.tensor([1, 2], dtype=torch.int64)    # 64-bit (signed) integer\n",
        "print('\\ndtype when we force a datatype:')\n",
        "print('32-bit float: ', y0.dtype)\n",
        "print('32-bit integer: ', y1.dtype)\n",
        "print('64-bit integer: ', y2.dtype)\n",
        "\n",
        "# Other creation ops also take a dtype argument\n",
        "z0 = torch.ones(1, 2)  # Let torch choose for us\n",
        "z1 = torch.ones(1, 2, dtype=torch.int16) # 16-bit (signed) integer\n",
        "z2 = torch.ones(1, 2, dtype=torch.uint8) # 8-bit (unsigned) integer\n",
        "print('\\ntorch.ones with different dtypes')\n",
        "print('default dtype:', z0.dtype)\n",
        "print('16-bit integer:', z1.dtype)\n",
        "print('8-bit unsigned integer:', z2.dtype)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "W2reBgQmx_x4"
      },
      "source": [
        "We can **cast** a tensor to another datatype using the [`.to()`](https://pytorch.org/docs/stable/generated/torch.Tensor.to.html) method; there are also convenience methods like [`.float()`](https://pytorch.org/docs/stable/generated/torch.Tensor.float.html) and [`.long()`](https://pytorch.org/docs/stable/generated/torch.Tensor.long.html) that cast to particular datatypes:\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "sAMpwGsdyHAw"
      },
      "outputs": [],
      "source": [
        "x0 = torch.eye(3, dtype=torch.int64)\n",
        "x1 = x0.float()  # Cast to 32-bit float\n",
        "x2 = x0.double() # Cast to 64-bit float\n",
        "x3 = x0.to(torch.float32) # Alternate way to cast to 32-bit float\n",
        "x4 = x0.to(torch.float64) # Alternate way to cast to 64-bit float\n",
        "print('x0:', x0.dtype)\n",
        "print('x1:', x1.dtype)\n",
        "print('x2:', x2.dtype)\n",
        "print('x3:', x3.dtype)\n",
        "print('x4:', x4.dtype)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "k2O8Atl1wMB7"
      },
      "source": [
        "PyTorch provides several ways to create a tensor with the same datatype as another tensor:\n",
        "\n",
        "- PyTorch provides tensor constructors such as [`torch.zeros_like()`](https://pytorch.org/docs/stable/generated/torch.zeros_like.html) that create new tensors with the same shape and type as a given tensor\n",
        "- Tensor objects have instance methods such as [`.new_zeros()`](https://pytorch.org/docs/stable/generated/torch.Tensor.new_zeros.html) that create tensors the same type but possibly different shapes\n",
        "- The tensor instance method [`.to()`](https://pytorch.org/docs/stable/generated/torch.Tensor.to.html) can take a tensor as an argument, in which case it casts to the datatype of the argument."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "1APDsx54xV6p"
      },
      "outputs": [],
      "source": [
        "x0 = torch.eye(3, dtype=torch.float64)  # Shape (3, 3), dtype torch.float64\n",
        "x1 = torch.zeros_like(x0)               # Shape (3, 3), dtype torch.float64\n",
        "x2 = x0.new_zeros(4, 5)                 # Shape (4, 5), dtype torch.float64\n",
        "x3 = torch.ones(6, 7).to(x0)            # Shape (6, 7), dtype torch.float64)\n",
        "print('x0 shape is %r, dtype is %r' % (x0.shape, x0.dtype))\n",
        "print('x1 shape is %r, dtype is %r' % (x1.shape, x1.dtype))\n",
        "print('x2 shape is %r, dtype is %r' % (x2.shape, x2.dtype))\n",
        "print('x3 shape is %r, dtype is %r' % (x3.shape, x3.dtype))"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "OPuGPa0v4h_2"
      },
      "source": [
        "**Your turn**: In the file `pytorch101.py`, implement the function `multiples_of_ten` which should create and return a tensor of dtype `torch.float64` containing all the multiples of ten in a given range.\n",
        "\n",
        "Hint: [`torch.arange`](https://pytorch.org/docs/stable/generated/torch.arange.html)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "Qddo6C5Bgwcr"
      },
      "outputs": [],
      "source": [
        "from pytorch101 import multiples_of_ten\n",
        "\n",
        "start = 5\n",
        "stop = 25\n",
        "x = multiples_of_ten(start, stop)\n",
        "print('Correct dtype: ', x.dtype == torch.float64)\n",
        "print('Correct shape: ', x.shape == (2,))\n",
        "print('Correct values: ', x.tolist() == [10, 20])\n",
        "\n",
        "# If there are no multiples of ten in the given range you should return an empty tensor\n",
        "start = 5\n",
        "stop = 7\n",
        "x = multiples_of_ten(start, stop)\n",
        "print('\\nCorrect dtype: ', x.dtype == torch.float64)\n",
        "print('Correct shape: ', x.shape == (0,))"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "RwJL3HVySvXn"
      },
      "source": [
        "Even though PyTorch provides a large number of numeric datatypes, the most commonly used datatypes are:\n",
        "\n",
        "- `torch.float32`: Standard floating-point type; used to store learnable parameters, network activations, etc. Nearly all arithmetic is done using this type.\n",
        "- `torch.int64`: Typically used to store indices\n",
        "- `torch.bool`: Stores boolean values: 0 is false and 1 is true\n",
        "- `torch.float16`: Used for mixed-precision arithmetic, usually on NVIDIA GPUs with [tensor cores](https://www.nvidia.com/en-us/data-center/tensorcore/). You won't need to worry about this datatype in this course."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "rlANfnILvX3S"
      },
      "source": [
        "## Tensor indexing"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "KP4dRrHhyLO5"
      },
      "source": [
        "We have already seen how to get and set individual elements of PyTorch tensors. PyTorch also provides many other ways of indexing into tensors. Getting comfortable with these different options makes it easy to modify different parts of tensors with ease."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "mo-PoTWNvbba"
      },
      "source": [
        "### Slice indexing"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "qUqTYvglyVLc"
      },
      "source": [
        "Similar to Python lists and numpy arrays, PyTorch tensors can be **sliced** using the syntax `start:stop` or `start:stop:step`. The `stop` index is always non-inclusive: it is the first element not to be included in the slice.\n",
        "\n",
        "Start and stop indices can be negative, in which case they count backward from the end of the tensor."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "yEr5BzdUdCtZ"
      },
      "outputs": [],
      "source": [
        "a = torch.tensor([0, 11, 22, 33, 44, 55, 66])\n",
        "print(0, a)        # (0) Original tensor\n",
        "print(1, a[2:5])   # (1) Elements between index 2 and 5\n",
        "print(2, a[2:])    # (2) Elements after index 2\n",
        "print(3, a[:5])    # (3) Elements before index 5\n",
        "print(4, a[:])     # (4) All elements\n",
        "print(5, a[1:5:2]) # (5) Every second element between indices 1 and 5\n",
        "print(6, a[:-1])   # (6) All but the last element\n",
        "print(7, a[-4::2]) # (7) Every second element, starting from the fourth-last"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "yrcr9PojgTS1"
      },
      "source": [
        "For multidimensional tensors, you can provide a slice or integer for each dimension of the tensor in order to extract different types of subtensors:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "S5fOdjTUyhNf"
      },
      "outputs": [],
      "source": [
        "# Create the following rank 2 tensor with shape (3, 4)\n",
        "# [[ 1  2  3  4]\n",
        "#  [ 5  6  7  8]\n",
        "#  [ 9 10 11 12]]\n",
        "a = torch.tensor([[1,2,3,4], [5,6,7,8], [9,10,11,12]])\n",
        "print('Original tensor:')\n",
        "print(a)\n",
        "print('shape: ', a.shape)\n",
        "\n",
        "# Get row 1, and all columns.\n",
        "print('\\nSingle row:')\n",
        "print(a[1, :])\n",
        "print(a[1])  # Gives the same result; we can omit : for trailing dimensions\n",
        "print('shape: ', a[1].shape)\n",
        "\n",
        "print('\\nSingle column:')\n",
        "print(a[:, 1])\n",
        "print('shape: ', a[:, 1].shape)\n",
        "\n",
        "# Get the first two rows and the last three columns\n",
        "print('\\nFirst two rows, last two columns:')\n",
        "print(a[:2, -3:])\n",
        "print('shape: ', a[:2, -3:].shape)\n",
        "\n",
        "# Get every other row, and columns at index 1 and 2\n",
        "print('\\nEvery other row, middle columns:')\n",
        "print(a[::2, 1:3])\n",
        "print('shape: ', a[::2, 1:3].shape)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "gOsR8Pdertku"
      },
      "source": [
        "There are two common ways to access a single row or column of a tensor: using an integer will reduce the rank by one, and using a length-one slice will keep the same rank. Note that this is different behavior from MATLAB."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "P1kHcc5jsF-c"
      },
      "outputs": [],
      "source": [
        "# Create the following rank 2 tensor with shape (3, 4)\n",
        "a = torch.tensor([[1,2,3,4], [5,6,7,8], [9,10,11,12]])\n",
        "print('Original tensor')\n",
        "print(a)\n",
        "\n",
        "row_r1 = a[1, :]    # Rank 1 view of the second row of a\n",
        "row_r2 = a[1:2, :]  # Rank 2 view of the second row of a\n",
        "print('\\nTwo ways of accessing a single row:')\n",
        "print(row_r1, row_r1.shape)\n",
        "print(row_r2, row_r2.shape)\n",
        "\n",
        "# We can make the same distinction when accessing columns:\n",
        "col_r1 = a[:, 1]\n",
        "col_r2 = a[:, 1:2]\n",
        "print('\\nTwo ways of accessing a single column:')\n",
        "print(col_r1, col_r1.shape)\n",
        "print(col_r2, col_r2.shape)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Jk625fJfyxV8"
      },
      "source": [
        "Slicing a tensor returns a **view** into the same data, so modifying it will also modify the original tensor. To avoid this, you can use the `clone()` method to make a copy of a tensor."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "IXbikYPwyxGA"
      },
      "outputs": [],
      "source": [
        "# Create a tensor, a slice, and a clone of a slice\n",
        "a = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8]])\n",
        "b = a[0, 1:]\n",
        "c = a[0, 1:].clone()\n",
        "print('Before mutating:')\n",
        "print(a)\n",
        "print(b)\n",
        "print(c)\n",
        "\n",
        "a[0, 1] = 20  # a[0, 1] and b[0] point to the same element\n",
        "b[1] = 30     # b[1] and a[0, 2] point to the same element\n",
        "c[2] = 40     # c is a clone, so it has its own data\n",
        "print('\\nAfter mutating:')\n",
        "print(a)\n",
        "print(b)\n",
        "print(c)\n",
        "\n",
        "print(a.storage().data_ptr() == c.storage().data_ptr())"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "5t5omyKwm9dB"
      },
      "source": [
        "**Your turn**: In the file `pytorch101.py`, implement the function `slice_indexing_practice` to practice indexing tensors with different types of slices."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "yKq2mswvqMmw"
      },
      "outputs": [],
      "source": [
        "# We will use this helper function to check your results\n",
        "def check(orig, actual, expected):\n",
        "    if not torch.is_tensor(actual):\n",
        "        return False\n",
        "    expected = torch.tensor(expected)\n",
        "    same_elements = (actual == expected).all().item()\n",
        "    same_storage = (orig.storage().data_ptr() == actual.storage().data_ptr())\n",
        "    return same_elements and same_storage"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 33,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5-5UtVXPVTQL",
        "outputId": "6c47f6d2-e5c8-4e78-aeb4-76ee97311e89"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "last_row:\n",
            "tensor([11, 12, 13, 14, 15])\n",
            "Correct: True\n",
            "\n",
            "third_col:\n",
            "tensor([[ 3],\n",
            "        [ 8],\n",
            "        [13]])\n",
            "Correct: True\n",
            "\n",
            "first_two_rows_three_cols:\n",
            "tensor([[1, 2, 3],\n",
            "        [6, 7, 8]])\n",
            "Correct: True\n",
            "\n",
            "even_rows_odd_cols:\n",
            "tensor([[ 2,  4],\n",
            "        [12, 14]])\n",
            "Correct: True\n",
            "\n"
          ]
        }
      ],
      "source": [
        "from pytorch101 import slice_indexing_practice\n",
        "\n",
        "# Create the following rank 2 tensor of shape (3, 5)\n",
        "# [[ 1  2  3  4  5]\n",
        "#  [ 6  7  8  9 10]\n",
        "#  [11 12 13 14 15]]\n",
        "x = torch.tensor([[1, 2, 3, 4, 5], [6, 7, 8, 8, 10], [11, 12, 13, 14, 15]])\n",
        "out = slice_indexing_practice(x)\n",
        "\n",
        "last_row = out[0]\n",
        "print('last_row:')\n",
        "print(last_row)\n",
        "correct = check(x, last_row, [11, 12, 13, 14, 15])\n",
        "print('Correct: %r\\n' % correct)\n",
        "\n",
        "third_col = out[1]\n",
        "print('third_col:')\n",
        "print(third_col)\n",
        "correct = check(x, third_col, [[3], [8], [13]])\n",
        "print('Correct: %r\\n' % correct)\n",
        "\n",
        "first_two_rows_three_cols = out[2]\n",
        "print('first_two_rows_three_cols:')\n",
        "print(first_two_rows_three_cols)\n",
        "correct = check(x, first_two_rows_three_cols, [[1, 2, 3], [6, 7, 8]])\n",
        "print('Correct: %r\\n' % correct)\n",
        "\n",
        "even_rows_odd_cols = out[3]\n",
        "print('even_rows_odd_cols:')\n",
        "print(even_rows_odd_cols)\n",
        "correct = check(x, even_rows_odd_cols, [[2, 4], [12, 14]])\n",
        "print('Correct: %r\\n' % correct)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "RNjhLwb0xY2A"
      },
      "source": [
        "So far we have used slicing to **access** subtensors; we can also use slicing to **modify** subtensors by writing assignment expressions where the left-hand side is a slice expression, and the right-hand side is a constant or a tensor of the correct shape:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "DFnky42Rx2I5"
      },
      "outputs": [],
      "source": [
        "a = torch.zeros(2, 4, dtype=torch.int64)\n",
        "a[:, :2] = 1\n",
        "a[:, 2:] = torch.tensor([[2, 3], [4, 5]])\n",
        "print(a)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "HPVCQ5HszihV"
      },
      "source": [
        "**Your turn**: in the file `pytorch101.py`, implement the function `slice_assignment_practice` to practice modifying tensors with slicing assignment statements.\n",
        "\n",
        "This function should use slicing assignment operations to modify the first four rows and first six columns of the input tensor so they are equal to\n",
        "\n",
        "$$\n",
        "\\begin{bmatrix}\n",
        "0 & 1 & 2 & 2 & 2 & 2 \\\\\n",
        "0 & 1 & 2 & 2 & 2 & 2 \\\\\n",
        "3 & 4 & 3 & 4 & 5 & 5 \\\\\n",
        "3 & 4 & 3 & 4 & 5 & 5 \\\\\n",
        "\\end{bmatrix}\n",
        "$$\n",
        "\n",
        "Your implementation must obey the following:\n",
        "- You should mutate the tensor x in-place and return it\n",
        "- You should only modify the first 4 rows and first 6 columns; all other\n",
        "elements should remain unchanged\n",
        "- You may only mutate the tensor using slice assignment operations, where you\n",
        "assign an integer to a slice of the tensor\n",
        "- You must use <= 6 slicing operations to achieve the desired result"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 35,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "FzXlnFqAVTQQ",
        "outputId": "a707d44f-ba3f-49b7-da5d-2d92bd8bcae0"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Here is x before calling slice_assignment_practice:\n",
            "tensor([[0, 0, 0, 0, 0, 0, 0],\n",
            "        [0, 0, 0, 0, 0, 0, 0],\n",
            "        [0, 0, 0, 0, 0, 0, 0],\n",
            "        [0, 0, 0, 0, 0, 0, 0],\n",
            "        [0, 0, 0, 0, 0, 0, 0]])\n",
            "Here is x after calling slice assignment practice:\n",
            "tensor([[0, 1, 2, 2, 2, 2, 0],\n",
            "        [0, 1, 2, 2, 2, 2, 0],\n",
            "        [3, 4, 3, 4, 5, 5, 0],\n",
            "        [3, 4, 3, 4, 5, 5, 0],\n",
            "        [0, 0, 0, 0, 0, 0, 0]])\n",
            "Correct:  True\n"
          ]
        }
      ],
      "source": [
        "from pytorch101 import slice_assignment_practice\n",
        "\n",
        "# note: this \"x\" has one extra row, intentionally\n",
        "x = torch.zeros(5, 7, dtype=torch.int64)\n",
        "print('Here is x before calling slice_assignment_practice:')\n",
        "print(x)\n",
        "slice_assignment_practice(x)\n",
        "print('Here is x after calling slice assignment practice:')\n",
        "print(x)\n",
        "\n",
        "expected = [\n",
        "    [0, 1, 2, 2, 2, 2, 0],\n",
        "    [0, 1, 2, 2, 2, 2, 0],\n",
        "    [3, 4, 3, 4, 5, 5, 0],\n",
        "    [3, 4, 3, 4, 5, 5, 0],\n",
        "    [0, 0, 0, 0, 0, 0, 0],\n",
        "]\n",
        "print('Correct: ', x.tolist() == expected)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "4y93rPhGveWw"
      },
      "source": [
        "### Integer tensor indexing"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "GlTyhjEN0AIE"
      },
      "source": [
        "When you index into torch tensor using slicing, the resulting tensor view will always be a subarray of the original tensor. This is powerful, but can be restrictive.\n",
        "\n",
        "We can also use **index arrays** to index tensors; this lets us construct new tensors with a lot more flexibility than using slices.\n",
        "\n",
        "As an example, we can use index arrays to reorder the rows or columns of a tensor:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "IXePPNkjM_SD"
      },
      "outputs": [],
      "source": [
        "# Create the following rank 2 tensor with shape (3, 4)\n",
        "# [[ 1  2  3  4]\n",
        "#  [ 5  6  7  8]\n",
        "#  [ 9 10 11 12]]\n",
        "a = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])\n",
        "print('Original tensor:')\n",
        "print(a)\n",
        "\n",
        "# Create a new tensor of shape (5, 4) by reordering rows from a:\n",
        "# - First two rows same as the first row of a\n",
        "# - Third row is the same as the last row of a\n",
        "# - Fourth and fifth rows are the same as the second row from a\n",
        "idx = [0, 0, 2, 1, 1]  # index arrays can be Python lists of integers\n",
        "print('\\nReordered rows:')\n",
        "print(a[idx])\n",
        "\n",
        "# Create a new tensor of shape (3, 4) by reversing the columns from a\n",
        "idx = torch.tensor([3, 2, 1, 0])  # Index arrays can be int64 torch tensors\n",
        "print('\\nReordered columns:')\n",
        "print(a[:, idx])"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "CpIBR1bCQji6"
      },
      "source": [
        "More generally, given index arrays `idx0` and `idx1` with `N` elements each, `a[idx0, idx1]` is equivalent to:\n",
        "\n",
        "```\n",
        "torch.tensor([\n",
        "  a[idx0[0], idx1[0]],\n",
        "  a[idx0[1], idx1[1]],\n",
        "  ...,\n",
        "  a[idx0[N - 1], idx1[N - 1]]\n",
        "])\n",
        "```\n",
        "\n",
        "(A similar pattern extends to tensors with more than two dimensions)\n",
        "\n",
        "We can for example use this to get or set the diagonal of a tensor:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "ocIR8R5ZSEaP"
      },
      "outputs": [],
      "source": [
        "a = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])\n",
        "print('Original tensor:')\n",
        "print(a)\n",
        "\n",
        "idx = [0, 1, 2]\n",
        "print('\\nGet the diagonal:')\n",
        "print(a[idx, idx])\n",
        "\n",
        "# Modify the diagonal\n",
        "a[idx, idx] = torch.tensor([11, 22, 33])\n",
        "print('\\nAfter setting the diagonal:')\n",
        "print(a)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "O-cr-EqA0vfO"
      },
      "source": [
        "One useful trick with integer array indexing is selecting or mutating one element from each row or column of a matrix:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "HWA8E8iI0x17"
      },
      "outputs": [],
      "source": [
        "# Create a new tensor from which we will select elements\n",
        "a = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])\n",
        "print('Original tensor:')\n",
        "print(a)\n",
        "\n",
        "# Take on element from each row of a:\n",
        "# from row 0, take element 1;\n",
        "# from row 1, take element 2;\n",
        "# from row 2, take element 1;\n",
        "# from row 3, take element 0\n",
        "idx0 = torch.arange(a.shape[0])  # Quick way to build [0, 1, 2, 3]\n",
        "idx1 = torch.tensor([1, 2, 1, 0])\n",
        "print('\\nSelect one element from each row:')\n",
        "print(a[idx0, idx1])\n",
        "\n",
        "# Now set each of those elements to zero\n",
        "a[idx0, idx1] = 0\n",
        "print('\\nAfter modifying one element from each row:')\n",
        "print(a)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "s5_-WUmSVEoR"
      },
      "source": [
        "**Your turn**: in the file `pytorch101.py`, implement the functions `shuffle_cols`, `reverse_rows`, and `take_one_elem_per_col` to practice using integer indexing to manipulate tensors. In each of these functions, your implementation should construct the output tensor **using a single indexing operation on the input**."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "FX05_ov5VTQZ"
      },
      "outputs": [],
      "source": [
        "from pytorch101 import shuffle_cols, reverse_rows, take_one_elem_per_col\n",
        "\n",
        "# Build a tensor of shape (4, 3):\n",
        "# [[ 1,  2,  3],\n",
        "#  [ 4,  5,  6],\n",
        "#  [ 7,  8,  9],\n",
        "#  [10, 11, 12]]\n",
        "x = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])\n",
        "print('Here is x:')\n",
        "print(x)\n",
        "\n",
        "y1 = shuffle_cols(x)\n",
        "print('\\nHere is shuffle_cols(x):')\n",
        "print(y1)\n",
        "expected = [[1, 1, 3, 2], [4, 4, 6, 5], [7, 7, 9, 8], [10, 10, 12, 11]]\n",
        "y1_correct = torch.is_tensor(y1) and y1.tolist() == expected\n",
        "print('Correct: %r\\n' % y1_correct)\n",
        "\n",
        "y2 = reverse_rows(x)\n",
        "print('Here is reverse_rows(x):')\n",
        "print(y2)\n",
        "expected = [[10, 11, 12], [7, 8, 9], [4, 5, 6], [1, 2, 3]]\n",
        "y2_correct = torch.is_tensor(y2) and y2.tolist() == expected\n",
        "print('Correct: %r\\n' % y2_correct)\n",
        "\n",
        "y3 = take_one_elem_per_col(x)\n",
        "print('Here is take_one_elem_per_col(x):')\n",
        "print(y3)\n",
        "expected = [4, 2, 12]\n",
        "y3_correct = torch.is_tensor(y3) and y3.tolist() == expected\n",
        "print('Correct: %r' % y3_correct)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Q68ZApgH31W9"
      },
      "source": [
        "Now implement the function `make_one_hot` that creates a matrix of **one-hot vectors** from a list of Python integers.\n",
        "\n",
        "A one-hot vector for an integer $n$ is a vector that has a one in its $n$th slot, and zeros in all other slots. One-hot vectors are commonly used to represent categorical variables in machine learning models.\n",
        "\n",
        "For example, given a list `[1, 4, 3, 2]` of integers, your function should produce the tensor:\n",
        "\n",
        "```\n",
        "[[0 1 0 0 0],\n",
        " [0 0 0 0 1],\n",
        " [0 0 0 1 0],\n",
        " [0 0 1 0 0]]\n",
        "```\n",
        "\n",
        "Here the first row corresponds to the first element of the list: it has a one at index 1, and zeros at all other indices. The second row corresponds to the second element of the list: it has a one at index 4, and zeros at all other indices. The other rows follow the same pattern. The output has just enough columns so that none of the rows go out-of-bounds: the largest index in the input is 4, so the output matrix has 5 columns."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "jaT1kuQ37Rsq"
      },
      "outputs": [],
      "source": [
        "from pytorch101 import make_one_hot\n",
        "\n",
        "def check_one_hot(x, y):\n",
        "    C = y.shape[1]\n",
        "    for i, n in enumerate(x):\n",
        "        if n >= C: return False\n",
        "        for j in range(C):\n",
        "            expected = 1.0 if j == n else 0.0\n",
        "            if y[i, j].item() != expected: return False\n",
        "        return True\n",
        "\n",
        "x0 = [1, 4, 3, 2]\n",
        "y0 = make_one_hot(x0)\n",
        "print('Here is y0:')\n",
        "print(y0)\n",
        "print('y0 correct: ', check_one_hot(x0, y0))\n",
        "\n",
        "x1 = [1, 3, 5, 7, 6, 2]\n",
        "y1 = make_one_hot(x1)\n",
        "print('\\nHere is y1:')\n",
        "print(y1)\n",
        "print('y1 correct: ', check_one_hot(x1, y1))"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "oGt8ZPb_vixw"
      },
      "source": [
        "### Boolean tensor indexing"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "6CkQaRj01xmU"
      },
      "source": [
        "Boolean tensor indexing lets you pick out arbitrary elements of a tensor according to a boolean mask. Frequently this type of indexing is used to select or modify the elements of a tensor that satisfy some condition.\n",
        "\n",
        "In PyTorch, we use tensors of dtype `torch.bool` to hold boolean masks.\n",
        "\n",
        "(Prior to version 1.2.0, there was no `torch.bool` type so instead `torch.uint8` was usually used to represent boolean data, with 0 indicating false and 1 indicating true. Watch out for this in older PyTorch code!)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "29Zf7rb82Dkd"
      },
      "outputs": [],
      "source": [
        "a = torch.tensor([[1,2], [3, 4], [5, 6]])\n",
        "print('Original tensor:')\n",
        "print(a)\n",
        "\n",
        "# Find the elements of a that are bigger than 3. The mask has the same shape as\n",
        "# a, where each element of mask tells whether the corresponding element of a\n",
        "# is greater than three.\n",
        "mask = (a > 3)\n",
        "print('\\nMask tensor:')\n",
        "print(mask)\n",
        "\n",
        "# We can use the mask to construct a rank-1 tensor containing the elements of a\n",
        "# that are selected by the mask\n",
        "print('\\nSelecting elements with the mask:')\n",
        "print(a[mask])\n",
        "\n",
        "# We can also use boolean masks to modify tensors; for example this sets all\n",
        "# elements <= 3 to zero:\n",
        "a[a <= 3] = 0\n",
        "print('\\nAfter modifying with a mask:')\n",
        "print(a)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "LtSmmMGodrTX"
      },
      "source": [
        "**Your turn**: In the file `pytorch101.py`, implement the function `sum_positive_entries` which computes the sum of all positive entries in a torch tensor. You can easily accomplish this using boolean tensor indexing. Your implementation should perform only a single indexing operation on the input tensor."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "2hkeYXN9d5xh"
      },
      "outputs": [],
      "source": [
        "from pytorch101 import sum_positive_entries\n",
        "\n",
        "# Make a few test cases\n",
        "torch.manual_seed(598)\n",
        "x0 = torch.tensor([[-1, -1, 0], [0, 1, 2], [3, 4, 5]])\n",
        "x1 = torch.tensor([-100, 0, 1, 2, 3])\n",
        "x2 = torch.randn(100, 100).long()\n",
        "print('Correct for x0: ', sum_positive_entries(x0) == 15)\n",
        "print('Correct for x1: ', sum_positive_entries(x1) == 6)\n",
        "print('Correct for x2: ', sum_positive_entries(x2) == 1871)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Ad-xqELwyqpN"
      },
      "source": [
        "## Reshaping operations"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Ql9_eXuU4OG8"
      },
      "source": [
        "### View"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "xfPb_2BY0HKw"
      },
      "source": [
        "PyTorch provides many ways to manipulate the shapes of tensors. The simplest example is [`.view()`](https://pytorch.org/docs/stable/generated/torch.Tensor.view.html): This returns a new tensor with the same number of elements as its input, but with a different shape.\n",
        "\n",
        "We can use `.view()` to flatten matrices into vectors, and to convert rank-1 vectors into rank-2 row or column matrices:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "kw-M7C_61FZK"
      },
      "outputs": [],
      "source": [
        "x0 = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8]])\n",
        "print('Original tensor:')\n",
        "print(x0)\n",
        "print('shape:', x0.shape)\n",
        "\n",
        "# Flatten x0 into a rank 1 vector of shape (8,)\n",
        "x1 = x0.view(8)\n",
        "print('\\nFlattened tensor:')\n",
        "print(x1)\n",
        "print('shape:', x1.shape)\n",
        "\n",
        "# Convert x1 to a rank 2 \"row vector\" of shape (1, 8)\n",
        "x2 = x1.view(1, 8)\n",
        "print('\\nRow vector:')\n",
        "print(x2)\n",
        "print('shape:', x2.shape)\n",
        "\n",
        "# Convert x1 to a rank 2 \"column vector\" of shape (8, 1)\n",
        "x3 = x1.view(8, 1)\n",
        "print('\\nColumn vector:')\n",
        "print(x3)\n",
        "print('shape:', x3.shape)\n",
        "\n",
        "# Convert x1 to a rank 3 tensor of shape (2, 2, 2):\n",
        "x4 = x1.view(2, 2, 2)\n",
        "print('\\nRank 3 tensor:')\n",
        "print(x4)\n",
        "print('shape:', x4.shape)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "eHsZ8BPF2PEq"
      },
      "source": [
        "As a convenience, calls to `.view()` may include a single -1 argument; this puts enough elements on that dimension so that the output has the same number of elements as the input. This makes it easy to write some reshape operations in a way that is agnostic to the shape of the tensor:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "qNWu-R_J2qFY"
      },
      "outputs": [],
      "source": [
        "# We can reuse these functions for tensors of different shapes\n",
        "def flatten(x):\n",
        "    return x.view(-1)\n",
        "\n",
        "def make_row_vec(x):\n",
        "    return x.view(1, -1)\n",
        "\n",
        "x0 = torch.tensor([[1, 2, 3], [4, 5, 6]])\n",
        "x0_flat = flatten(x0)\n",
        "x0_row = make_row_vec(x0)\n",
        "print('x0:')\n",
        "print(x0)\n",
        "print('x0_flat:')\n",
        "print(x0_flat)\n",
        "print('x0_row:')\n",
        "print(x0_row)\n",
        "\n",
        "x1 = torch.tensor([[1, 2], [3, 4]])\n",
        "x1_flat = flatten(x1)\n",
        "x1_row = make_row_vec(x1)\n",
        "print('\\nx1:')\n",
        "print(x1)\n",
        "print('x1_flat:')\n",
        "print(x1_flat)\n",
        "print('x1_row:')\n",
        "print(x1_row)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "DK-ZB5aB2NPq"
      },
      "source": [
        "As its name implies, a tensor returned by `.view()` shares the same data as the input, so changes to one will affect the other and vice-versa:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "ebT99rUo2McN"
      },
      "outputs": [],
      "source": [
        "x = torch.tensor([[1, 2, 3], [4, 5, 6]])\n",
        "x_flat = x.view(-1)\n",
        "print('x before modifying:')\n",
        "print(x)\n",
        "print('x_flat before modifying:')\n",
        "print(x_flat)\n",
        "\n",
        "x[0, 0] = 10   # x[0, 0] and x_flat[0] point to the same data\n",
        "x_flat[1] = 20 # x_flat[1] and x[0, 1] point to the same data\n",
        "\n",
        "print('\\nx after modifying:')\n",
        "print(x)\n",
        "print('x_flat after modifying:')\n",
        "print(x_flat)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Z150qBob4Wkz"
      },
      "source": [
        "### Swapping axes"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "TCMDxbyBys78"
      },
      "source": [
        "Another common reshape operation you might want to perform is transposing a matrix. You might be surprised if you try to transpose a matrix with `.view()`: The `view()` function takes elements in row-major order, so **you cannot transpose matrices with `.view()`**.\n",
        "\n",
        "In general, you should only use `.view()` to add new dimensions to a tensor, or to collapse adjacent dimensions of a tensor.\n",
        "\n",
        "For other types of reshape operations, you usually need to use a function that can swap axes of a tensor. The simplest such function is `.t()`, specificially for transposing matrices. It is available both as a [function in the `torch` module](https://pytorch.org/docs/stable/generated/torch.t.html#torch.t), and as a [tensor instance method](https://pytorch.org/docs/stable/generated/torch.Tensor.t.html):"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "o_B4NuX6zQm-"
      },
      "outputs": [],
      "source": [
        "x = torch.tensor([[1, 2, 3], [4, 5, 6]])\n",
        "print('Original matrix:')\n",
        "print(x)\n",
        "print('\\nTransposing with view DOES NOT WORK!')\n",
        "print(x.view(3, 2))\n",
        "print('\\nTransposed matrix:')\n",
        "print(torch.t(x))\n",
        "print(x.t())"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "RN93xo98zn0v"
      },
      "source": [
        "For tensors with more than two dimensions, we can use the function [`torch.transpose`](https://pytorch.org/docs/stable/generated/torch.transpose.html) (or its [instance method variant](https://pytorch.org/docs/stable/generated/torch.Tensor.transpose.html)) to swap arbitrary dimensions.\n",
        "\n",
        "If you want to swap multiple axes at the same time, you can use [`torch.permute`](https://pytorch.org/docs/stable/generated/torch.permute.html) (or its [instance method variant](https://pytorch.org/docs/stable/generated/torch.Tensor.permute.html)) method to arbitrarily permute dimensions:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "XgN7YB8YzzkA"
      },
      "outputs": [],
      "source": [
        "# Create a tensor of shape (2, 3, 4)\n",
        "x0 = torch.tensor([\n",
        "     [[1,  2,  3,  4],\n",
        "      [5,  6,  7,  8],\n",
        "      [9, 10, 11, 12]],\n",
        "     [[13, 14, 15, 16],\n",
        "      [17, 18, 19, 20],\n",
        "      [21, 22, 23, 24]]])\n",
        "print('Original tensor:')\n",
        "print(x0)\n",
        "print('shape:', x0.shape)\n",
        "\n",
        "# Swap axes 1 and 2; shape is (2, 4, 3)\n",
        "x1 = x0.transpose(1, 2)\n",
        "print('\\nSwap axes 1 and 2:')\n",
        "print(x1)\n",
        "print(x1.shape)\n",
        "\n",
        "# Permute axes; the argument (1, 2, 0) means:\n",
        "# - Make the old dimension 1 appear at dimension 0;\n",
        "# - Make the old dimension 2 appear at dimension 1;\n",
        "# - Make the old dimension 0 appear at dimension 2\n",
        "# This results in a tensor of shape (3, 4, 2)\n",
        "x2 = x0.permute(1, 2, 0)\n",
        "print('\\nPermute axes')\n",
        "print(x2)\n",
        "print('shape:', x2.shape)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "f4SJCVbf-bZ0"
      },
      "source": [
        "### Contiguous tensors"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "ubOOujO_-pQT"
      },
      "source": [
        "Some combinations of reshaping operations will fail with cryptic errors. The exact reasons for this have to do with the way that tensors and views of tensors are implemented, and are beyond the scope of this assignment. However if you're curious, [this blog post by Edward Yang](http://blog.ezyang.com/2019/05/pytorch-internals/) gives a clear explanation of the problem.\n",
        "\n",
        "What you need to know is that you can typically overcome these sorts of errors by either by calling [`.contiguous()`](https://pytorch.org/docs/stable/generated/torch.Tensor.contiguous.html) before `.view()`, or by using [`.reshape()`](https://pytorch.org/docs/stable/generated/torch.reshape.html) instead of `.view()`."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "YGC6NERq_CT9"
      },
      "outputs": [],
      "source": [
        "x0 = torch.randn(2, 3, 4)\n",
        "\n",
        "try:\n",
        "  # This sequence of reshape operations will crash\n",
        "  x1 = x0.transpose(1, 2).view(8, 3)\n",
        "except RuntimeError as e:\n",
        "  print(type(e), e)\n",
        "\n",
        "# We can solve the problem using either .contiguous() or .reshape()\n",
        "x1 = x0.transpose(1, 2).contiguous().view(8, 3)\n",
        "x2 = x0.transpose(1, 2).reshape(8, 3)\n",
        "print('x1 shape: ', x1.shape)\n",
        "print('x2 shape: ', x2.shape)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "WJiiBxNE-X8g"
      },
      "source": [
        "### **Your turn**"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "iOVzHiX-86Ew"
      },
      "source": [
        "In the file `pytorch101.py`, implement the function `reshape_practice` to practice using reshape operations on tensors. Given the 1-dimensional input tensor `x` containing the numbers 0 through 23 in order, it should the following output tensor `y` of shape `(3, 8)` by using reshape operations on x:\n",
        "\n",
        "\n",
        "```\n",
        "y = tensor([[ 0,  1,  2,  3, 12, 13, 14, 15],\n",
        "            [ 4,  5,  6,  7, 16, 17, 18, 19],\n",
        "            [ 8,  9, 10, 11, 20, 21, 22, 23]])\n",
        "```\n",
        "\n",
        "Hint: You will need to create an intermediate tensor of rank 3"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "8reAZGzFVTQ3"
      },
      "outputs": [],
      "source": [
        "from pytorch101 import reshape_practice\n",
        "\n",
        "x = torch.arange(24)\n",
        "print('Here is x:')\n",
        "print(x)\n",
        "y = reshape_practice(x)\n",
        "print('Here is y:')\n",
        "print(y)\n",
        "\n",
        "expected = [\n",
        "    [0, 1,  2,  3, 12, 13, 14, 15],\n",
        "    [4, 5,  6,  7, 16, 17, 18, 19],\n",
        "    [8, 9, 10, 11, 20, 21, 22, 23]]\n",
        "print('Correct:', y.tolist() == expected)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "NgcdvD1evxTQ"
      },
      "source": [
        "## Tensor operations\n",
        "So far we have seen how to construct, access, and reshape tensors. But one of the most important reasons to use tensors is for performing computation! PyTorch provides many different operations to perform computations on tensors."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "1BCVlPHZ4_Qz"
      },
      "source": [
        "### Elementwise operations"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "f2wbN18E5CKI"
      },
      "source": [
        "Basic mathematical functions operate elementwise on tensors, and are available as operator overloads, as functions in the `torch` module, and as instance methods on torch objects; all produce the same results:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "QrMkbk535KRZ"
      },
      "outputs": [],
      "source": [
        "x = torch.tensor([[1, 2, 3, 4]], dtype=torch.float32)\n",
        "y = torch.tensor([[5, 6, 7, 8]], dtype=torch.float32)\n",
        "\n",
        "# Elementwise sum; all give the same result\n",
        "print('Elementwise sum:')\n",
        "print(x + y)\n",
        "print(torch.add(x, y))\n",
        "print(x.add(y))\n",
        "\n",
        "# Elementwise difference\n",
        "print('\\nElementwise difference:')\n",
        "print(x - y)\n",
        "print(torch.sub(x, y))\n",
        "print(x.sub(y))\n",
        "\n",
        "# Elementwise product\n",
        "print('\\nElementwise product:')\n",
        "print(x * y)\n",
        "print(torch.mul(x, y))\n",
        "print(x.mul(y))\n",
        "\n",
        "# Elementwise division\n",
        "print('\\nElementwise division')\n",
        "print(x / y)\n",
        "print(torch.div(x, y))\n",
        "print(x.div(y))\n",
        "\n",
        "# Elementwise power\n",
        "print('\\nElementwise power')\n",
        "print(x ** y)\n",
        "print(torch.pow(x, y))\n",
        "print(x.pow(y))"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "A6WwPJMYlYvN"
      },
      "source": [
        "Torch also provides many standard mathematical functions; these are available both as functions in the `torch` module and as instance methods on tensors:\n",
        "\n",
        "You can find a full list of all available mathematical functions [in the documentation](https://pytorch.org/docs/stable/torch.html#pointwise-ops); many functions in the `torch` module have corresponding instance methods [on tensor objects](https://pytorch.org/docs/stable/tensors.html)."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "s87mjsnG58vR"
      },
      "outputs": [],
      "source": [
        "x = torch.tensor([[1, 2, 3, 4]], dtype=torch.float32)\n",
        "\n",
        "print('Square root:')\n",
        "print(torch.sqrt(x))\n",
        "print(x.sqrt())\n",
        "\n",
        "print('\\nTrig functions:')\n",
        "print(torch.sin(x))\n",
        "print(x.sin())\n",
        "print(torch.cos(x))\n",
        "print(x.cos())"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "yDyH9USAuyZ-"
      },
      "source": [
        "### Reduction operations"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "wbHP9SpZHoMO"
      },
      "source": [
        "So far we've seen basic arithmetic operations on tensors that operate elementwise. We may sometimes want to perform operations that aggregate over part or all of a tensor, such as a summation; these are called **reduction** operations.\n",
        "\n",
        "Like the elementwise operations above, most reduction operations are available both as functions in the `torch` module and as instance methods on `tensor` objects.\n",
        "\n",
        "The simplest reduction operation is summation. We can use the [`.sum()`](https://pytorch.org/docs/stable/generated/torch.Tensor.sum.html) method (or eqivalently [`torch.sum`](https://pytorch.org/docs/stable/generated/torch.sum.html)) to reduce either an entire tensor, or to reduce along only one dimension of the tensor using the `dim` argument:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "LlmsYJWUE2r3"
      },
      "outputs": [],
      "source": [
        "x = torch.tensor([[1, 2, 3],\n",
        "                  [4, 5, 6]], dtype=torch.float32)\n",
        "print('Original tensor:')\n",
        "print(x)\n",
        "\n",
        "print('\\nSum over entire tensor:')\n",
        "print(torch.sum(x))\n",
        "print(x.sum())\n",
        "\n",
        "# We can sum over the first dimension:\n",
        "print('\\nSum over the first dimension:')\n",
        "print(torch.sum(x, dim=0))\n",
        "print(x.sum(dim=0))\n",
        "\n",
        "# Sum over the second dimension:\n",
        "print('\\nSum over the second dimension:')\n",
        "print(torch.sum(x, dim=1))\n",
        "print(x.sum(dim=1))"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "qB09ong1ur1Q"
      },
      "source": [
        "Students often get confused by the `dim` argument in reduction operations -- how do I sum over rows vs columns?\n",
        "\n",
        "The easiest way to remember is to think about the shapes of the tensors involved.\n",
        "After summing with `dim=d`, the dimension at index `d` of the input is **eliminated** from the shape of the output tensor:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "OySNH7Spur1Q"
      },
      "outputs": [],
      "source": [
        "# Create a tensor of shape (3, 4, 5, 6)\n",
        "x = torch.randn(3, 4, 5, 6)\n",
        "print('x.shape: ', x.shape)\n",
        "\n",
        "# Summing over dim=0 eliminates the dimension at index 0 (of size 3):\n",
        "print('x.sum(dim=0).shape: ', x.sum(dim=0).shape)\n",
        "\n",
        "# Summing with dim=1 eliminates the dimension at index 1 (of size 4):\n",
        "print('x.sum(dim=1).shape: ', x.sum(dim=1).shape)\n",
        "\n",
        "# Summing with dim=2 eliminates the dimension at index 2 (of size 5):\n",
        "print('x.sum(dim=2).shape: ', x.sum(dim=2).shape)\n",
        "\n",
        "# Summing with dim=3 eliminates the dimension at index 3 (of size 6):\n",
        "print('x.sum(dim=3).shape: ', x.sum(dim=3).shape)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "DzKio_3Quz5a"
      },
      "source": [
        "Other useful reduction operations include [`mean`](https://pytorch.org/docs/stable/generated/torch.mean.html), [`min`](https://pytorch.org/docs/stable/generated/torch.min.html), and [`max`](https://pytorch.org/docs/stable/generated/torch.max.html). You can find a full list of all available reduction operations [in the documentation](https://pytorch.org/docs/stable/torch.html#reduction-ops).\n",
        "\n",
        "Some reduction operations return more than one value; for example `min` returns both the minimum value over the specified dimension, as well as the index where the minimum value occurs:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "TFD7aT54H4ik"
      },
      "outputs": [],
      "source": [
        "x = torch.tensor([[2, 4, 3, 5], [3, 3, 5, 2]], dtype=torch.float32)\n",
        "print('Original tensor:')\n",
        "print(x, x.shape)\n",
        "\n",
        "# Finding the overall minimum only returns a single value\n",
        "print('\\nOverall minimum: ', x.min())\n",
        "\n",
        "# Compute the minimum along each column; we get both the value and location:\n",
        "# The minimum of the first column is 2, and it appears at index 0;\n",
        "# the minimum of the second column is 3 and it appears at index 1; etc\n",
        "col_min_vals, col_min_idxs = x.min(dim=0)\n",
        "print('\\nMinimum along each column:')\n",
        "print('values:', col_min_vals)\n",
        "print('idxs:', col_min_idxs)\n",
        "\n",
        "# Compute the minimum along each row; we get both the value and the minimum\n",
        "row_min_vals, row_min_idxs = x.min(dim=1)\n",
        "print('\\nMinimum along each row:')\n",
        "print('values:', row_min_vals)\n",
        "print('idxs:', row_min_idxs)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "XFwYRESoFr4t"
      },
      "source": [
        "Reduction operations *reduce* the rank of tensors: the dimension over which you perform the reduction will be removed from the shape of the output. If you pass `keepdim=True` to a reduction operation, the specified dimension will not be removed; the output tensor will instead have a shape of 1 in that dimension.\n",
        "\n",
        "When you are working with multidimensional tensors, thinking about rows and columns can become confusing; instead it's more useful to think about the shape that will result from each operation. For example:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "sjcAveyJFqm7"
      },
      "outputs": [],
      "source": [
        "# Create a tensor of shape (128, 10, 3, 64, 64)\n",
        "x = torch.randn(128, 10, 3, 64, 64)\n",
        "print(x.shape)\n",
        "\n",
        "# Take the mean over dimension 1; shape is now (128, 3, 64, 64)\n",
        "x = x.mean(dim=1)\n",
        "print(x.shape)\n",
        "\n",
        "# Take the sum over dimension 2; shape is now (128, 3, 64)\n",
        "x = x.sum(dim=2)\n",
        "print(x.shape)\n",
        "\n",
        "# Take the mean over dimension 1, but keep the dimension from being eliminated\n",
        "# by passing keepdim=True; shape is now (128, 1, 64)\n",
        "x = x.mean(dim=1, keepdim=True)\n",
        "print(x.shape)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "gXMp4tcM0Q_E"
      },
      "source": [
        "**Your turn**: In the file `pytorch101.py`, implement the function `zero_row_min` which sets the minimum value along each row of a tensor to zero. You should use reduction and indexing operations, and you should not use any explicit loops.\n",
        "\n",
        "Hint: [`clone`](https://pytorch.org/docs/stable/generated/torch.Tensor.clone.html), [`argmin`](https://pytorch.org/docs/stable/generated/torch.Tensor.argmin.html)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "aaJzt-Y62blF"
      },
      "outputs": [],
      "source": [
        "from pytorch101 import zero_row_min\n",
        "\n",
        "x0 = torch.tensor([[10, 20, 30], [2, 5, 1]])\n",
        "print('Here is x0:')\n",
        "print(x0)\n",
        "y0 = zero_row_min(x0)\n",
        "print('Here is y0:')\n",
        "print(y0)\n",
        "expected = [[0, 20, 30], [2, 5, 0]]\n",
        "y0_correct = torch.is_tensor(y0) and y0.tolist() == expected\n",
        "print('y0 correct: ', y0_correct)\n",
        "\n",
        "x1 = torch.tensor([[2, 5, 10, -1], [1, 3, 2, 4], [5, 6, 2, 10]])\n",
        "print('\\nHere is x1:')\n",
        "print(x1)\n",
        "y1 = zero_row_min(x1)\n",
        "print('Here is y1:')\n",
        "print(y1)\n",
        "expected = [[2, 5, 10, 0], [0, 3, 2, 4], [5, 6, 0, 10]]\n",
        "y1_correct = torch.is_tensor(y1) and y1.tolist() == expected\n",
        "print('y1 correct: ', y1_correct)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "lRyLyXU2u29N"
      },
      "source": [
        "### Matrix operations"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "7DwjbapG6MM_"
      },
      "source": [
        "Note that unlike MATLAB, * is elementwise multiplication, not matrix multiplication. PyTorch provides a number of linear algebra functions that compute different types of vector and matrix products. The most commonly used are:\n",
        "\n",
        "- [`torch.dot`](https://pytorch.org/docs/stable/generated/torch.dot.html): Computes inner product of vectors\n",
        "- [`torch.mm`](https://pytorch.org/docs/stable/generated/torch.mm.html): Computes matrix-matrix products\n",
        "- [`torch.mv`](https://pytorch.org/docs/stable/generated/torch.mv.html): Computes matrix-vector products\n",
        "- [`torch.addmm`](https://pytorch.org/docs/stable/generated/torch.addmm.html) / [`torch.addmv`](https://pytorch.org/docs/stable/generated/torch.addmv.html): Computes matrix-matrix and matrix-vector multiplications plus a bias\n",
        "- [`torch.bmm`](https://pytorch.org/docs/stable/generated/torch.bmm.html) / [`torch.baddmm`](https://pytorch.org/docs/stable/generated/torch.baddbmm.html): Batched versions of `torch.mm` and `torch.addmm`, respectively\n",
        "- [`torch.matmul`](https://pytorch.org/docs/stable/generated/torch.matmul.html): General matrix product that performs different operations depending on the rank of the inputs. Confusingly, this is similar to `np.dot` in numpy.\n",
        "\n",
        "You can find a full list of the available linear algebra operators [in the documentation](https://pytorch.org/docs/stable/torch.html#blas-and-lapack-operations).\n",
        "All of these functions are also available as Tensor instance methods, e.g. [`Tensor.dot`](https://pytorch.org/docs/stable/generated/torch.Tensor.dot.html) instead of `torch.dot`.\n",
        "\n",
        "Here is an example of using `torch.dot` to compute inner products. Like the other mathematical operators we've seen, most linear algebra operators are available both as functions in the `torch` module and as instance methods of tensors:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "TRUYW2as6ZCh"
      },
      "outputs": [],
      "source": [
        "v = torch.tensor([9,10], dtype=torch.float32)\n",
        "w = torch.tensor([11, 12], dtype=torch.float32)\n",
        "\n",
        "# Inner product of vectors\n",
        "print('Dot products:')\n",
        "print(torch.dot(v, w))\n",
        "print(v.dot(w))\n",
        "\n",
        "# dot only works for vectors -- it will give an error for tensors of rank > 1\n",
        "x = torch.tensor([[1,2],[3,4]], dtype=torch.float32)\n",
        "y = torch.tensor([[5,6],[7,8]], dtype=torch.float32)\n",
        "try:\n",
        "  print(x.dot(y))\n",
        "except RuntimeError as e:\n",
        "  print(e)\n",
        "\n",
        "# Instead we use mm for matrix-matrix products:\n",
        "print('\\nMatrix-matrix product:')\n",
        "print(torch.mm(x, y))\n",
        "print(x.mm(y))"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "MQRxK34KdHm3"
      },
      "source": [
        "With all the different linear algebra operators that PyTorch provides, there is usually more than one way to compute something. For example to compute matrix-vector products we can use `torch.mv`; we can reshape the vector to have rank 2 and use `torch.mm`; or we can use `torch.matmul`. All give the same results, but the outputs might have different ranks:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "qqEzcnHkdRYA"
      },
      "outputs": [],
      "source": [
        "print('Here is x (rank 2):')\n",
        "print(x)\n",
        "print('\\nHere is v (rank 1):')\n",
        "print(v)\n",
        "\n",
        "# Matrix-vector multiply with torch.mv produces a rank-1 output\n",
        "print('\\nMatrix-vector product with torch.mv (rank 1 output)')\n",
        "print(torch.mv(x, v))\n",
        "print(x.mv(v))\n",
        "\n",
        "# We can reshape the vector to have rank 2 and use torch.mm to perform\n",
        "# matrix-vector products, but the result will have rank 2\n",
        "print('\\nMatrix-vector product with torch.mm (rank 2 output)')\n",
        "print(torch.mm(x, v.view(2, 1)))\n",
        "print(x.mm(v.view(2, 1)))\n",
        "\n",
        "print('\\nMatrix-vector product with torch.matmul (rank 1 output)')\n",
        "print(torch.matmul(x, v))\n",
        "print(x.matmul(v))"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "-eqQJ5IUjtNT"
      },
      "source": [
        "**Your turn**: In the file `pytorch101.py`, look at the function `batched_matrix_multiply`.\n",
        "\n",
        "You should implement the two variants `batched_matrix_multiply_loop` and `batched_matrix_multiply_noloop`; the first should use an explicit Python loop over the batch dimension, and the second should perform batched matrix multiplication using a single PyTorch operation with no explicit loops.\n",
        "\n",
        "Hint: [`torch.stack`](https://pytorch.org/docs/master/generated/torch.stack.html), [`torch.bmm`](https://pytorch.org/docs/stable/generated/torch.bmm.html) may be useful."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "sZD1VQHKVTRQ"
      },
      "outputs": [],
      "source": [
        "from pytorch101 import batched_matrix_multiply\n",
        "\n",
        "B, N, M, P = 2, 3, 5, 4\n",
        "x = torch.randn(B, N, M)\n",
        "y = torch.randn(B, M, P)\n",
        "z_expected = torch.stack([x[0] @ y[0], x[1] @ y[1]])\n",
        "\n",
        "# The two may not return exactly the same result; different linear algebra\n",
        "# routines often return slightly different results due to the fact that\n",
        "# floating-point math is non-exact and non-associative.\n",
        "z1 = batched_matrix_multiply(x, y, use_loop=True)\n",
        "z1_diff = (z1 - z_expected).abs().max().item()\n",
        "print('z1 difference: ', z1_diff)\n",
        "print('z1 difference within tolerance: ', z1_diff < 1e-6)\n",
        "\n",
        "z2 = batched_matrix_multiply(x, y, use_loop=False)\n",
        "z2_diff = (z2 - z_expected).abs().max().item()\n",
        "print('\\nz2 difference: ', z2_diff)\n",
        "print('z2 difference within tolerance: ', z2_diff < 1e-6)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "mbCVOr2sVTRR"
      },
      "source": [
        "### Vectorization\n",
        "In many cases, avoiding explicit Python loops in your code and instead using PyTorch operators to handle looping internally will cause your code to run a lot faster. This style of writing code, called **vectorization**, avoids overhead from the Python interpreter, and can also better parallelize the computation (e.g. across CPU cores, on on GPUs). Whenever possible you should strive to write vectorized code.\n",
        "\n",
        "Run the following the compare the speed of the `batched_matrix_multiply` with `use_loop=True` and with `use_loop=False`."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "a-acTIOpVTRR"
      },
      "outputs": [],
      "source": [
        "import time\n",
        "import matplotlib.pyplot as plt\n",
        "from pytorch101 import batched_matrix_multiply\n",
        "\n",
        "N, M, P = 64, 64, 64\n",
        "loop_times = []\n",
        "no_loop_times = []\n",
        "no_loop_speedup = []\n",
        "Bs = list(range(4, 128, 4))\n",
        "num_trials = 20\n",
        "for B in Bs:\n",
        "    loop_trials = []\n",
        "    no_loop_trials = []\n",
        "    for trial in range(num_trials):\n",
        "        x = torch.randn(B, N, M)\n",
        "        y = torch.randn(B, M, P)\n",
        "        t0 = time.time()\n",
        "        z1 = batched_matrix_multiply(x, y, use_loop=True)\n",
        "        t1 = time.time()\n",
        "        z2 = batched_matrix_multiply(x, y, use_loop=False)\n",
        "        t2 = time.time()\n",
        "        loop_trials.append(t1 - t0)\n",
        "        no_loop_trials.append(t2 - t1)\n",
        "    loop_mean = torch.tensor(loop_trials).mean().item()\n",
        "    no_loop_mean = torch.tensor(no_loop_trials).mean().item()\n",
        "    loop_times.append(loop_mean)\n",
        "    no_loop_times.append(no_loop_mean)\n",
        "    no_loop_speedup.append(loop_mean / no_loop_mean)\n",
        "\n",
        "plt.subplot(1, 2, 1)\n",
        "plt.plot(Bs, loop_times, 'o-', label='use_loop=True')\n",
        "plt.plot(Bs, no_loop_times, 'o-', label='use_loop=False')\n",
        "plt.xlabel('Batch size B')\n",
        "plt.ylabel('Runtime (s)')\n",
        "plt.legend(fontsize=14)\n",
        "plt.title('Loop vs Vectorized speeds')\n",
        "\n",
        "plt.subplot(1, 2, 2)\n",
        "plt.plot(Bs, no_loop_speedup, '-o')\n",
        "plt.title('Vectorized speedup')\n",
        "plt.xlabel('Batch size B')\n",
        "plt.ylabel('Vectorized speedup')\n",
        "\n",
        "plt.gcf().set_size_inches(12, 4)\n",
        "plt.show()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "UISn2pcf9QjY"
      },
      "source": [
        "## Broadcasting"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "fTj6f8VN9UZg"
      },
      "source": [
        "Broadcasting is a powerful mechanism that allows PyTorch to work with arrays of different shapes when performing arithmetic operations. Frequently we have a smaller tensor and a larger tensor, and we want to use the smaller tensor multiple times to perform some operation on the larger tensor.\n",
        "\n",
        "For example, suppose that we want to add a constant vector to each row of a tensor. We could do it like this:\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "kF0Dhzlu9fef"
      },
      "outputs": [],
      "source": [
        "# We will add the vector v to each row of the matrix x,\n",
        "# storing the result in the matrix y\n",
        "x = torch.tensor([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])\n",
        "v = torch.tensor([1, 0, 1])\n",
        "y = torch.zeros_like(x)   # Create an empty matrix with the same shape as x\n",
        "\n",
        "# Add the vector v to each row of the matrix x with an explicit loop\n",
        "for i in range(4):\n",
        "    y[i, :] = x[i, :] + v\n",
        "\n",
        "print(y)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "7gXpoBKE9vp7"
      },
      "source": [
        "This works; however when the tensor x is very large, computing an explicit loop in Python could be slow. Note that adding the vector v to each row of the tensor x is equivalent to forming a tensor vv by stacking multiple copies of v vertically, then performing elementwise summation of x and vv. We could implement this approach like this:\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "_2_5cKeu94c2"
      },
      "outputs": [],
      "source": [
        "vv = v.repeat((4, 1))  # Stack 4 copies of v on top of each other\n",
        "print(vv)              # Prints \"[[1 0 1]\n",
        "                       #          [1 0 1]\n",
        "                       #          [1 0 1]\n",
        "                       #          [1 0 1]]\""
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "1KiRj23p-QIs"
      },
      "outputs": [],
      "source": [
        "y = x + vv  # Add x and vv elementwise\n",
        "print(y)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "A7NNlSsHBKib"
      },
      "source": [
        "PyTorch broadcasting allows us to perform this computation without actually creating multiple copies of v. Consider this version, using broadcasting:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "2jIiZc-ABBnt"
      },
      "outputs": [],
      "source": [
        "# We will add the vector v to each row of the matrix x,\n",
        "# storing the result in the matrix y\n",
        "x = torch.tensor([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])\n",
        "v = torch.tensor([1, 0, 1])\n",
        "y = x + v  # Add v to each row of x using broadcasting\n",
        "print(y)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "HuUBX8YnBSIG"
      },
      "source": [
        "The line y = x + v works even though x has shape (4, 3) and v has shape (3,) due to broadcasting; this line works as if v actually had shape (4, 3), where each row was a copy of v, and the sum was performed elementwise.\n",
        "\n",
        "Broadcasting two tensors together follows these rules:\n",
        "\n",
        "1.   If the tensors do not have the same rank, prepend the shape of the lower rank array with 1s until both shapes have the same length.\n",
        "2.   The two tensors are said to be *compatible* in a dimension if they have the same size in the dimension, or if one of the tensors has size 1 in that dimension.\n",
        "3.   The tensors can be broadcast together if they are compatible in all dimensions.\n",
        "4.   After broadcasting, each tensor behaves as if it had shape equal to the elementwise maximum of shapes of the two input tensors.\n",
        "5.   In any dimension where one tensor had size 1 and the other tensor had size greater than 1, the first tensor behaves as if it were copied along that dimension\n",
        "\n",
        "If this explanation does not make sense, try reading the explanation from the [documentation](https://pytorch.org/docs/stable/notes/broadcasting.html).\n",
        "\n",
        "Broadcasting usually happens implicitly inside many PyTorch operators. However we can also broadcast explicitly using the function [`torch.broadcast_tensors`](https://pytorch.org/docs/stable/generated/torch.broadcast_tensors.html#torch.broadcast_tensors):"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "YIlIBao3VTRc"
      },
      "outputs": [],
      "source": [
        "x = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])\n",
        "v = torch.tensor([1, 0, 1])\n",
        "print('Here is x (before broadcasting):')\n",
        "print(x)\n",
        "print('x.shape: ', x.shape)\n",
        "print('\\nHere is v (before broadcasting):')\n",
        "print(v)\n",
        "print('v.shape: ', v.shape)\n",
        "\n",
        "xx, vv = torch.broadcast_tensors(x, v)\n",
        "print('Here is xx (after) broadcasting):')\n",
        "print(xx)\n",
        "print('xx.shape: ', x.shape)\n",
        "print('\\nHere is vv (after broadcasting):')\n",
        "print(vv)\n",
        "print('vv.shape: ', vv.shape)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "PWXtBo6eVTRf"
      },
      "source": [
        "Notice that after broadcasting, `x` remains the same but `v` has an extra dimension prepended to its shape, and it is duplicated to have the same shape as `x`; since they have the same shape after broadcasting they can be added elementwise.\n",
        "\n",
        "All elementwise functions support broadcasting.\n",
        "Some non-elementwise functions (such as linear algebra routines) also support broadcasting;\n",
        "you can check the documentation to tell whether any particular function supports broadcasting.\n",
        "For example [`torch.mm`](https://pytorch.org/docs/stable/generated/torch.mm.html) does not support broadcasting,\n",
        "but [`torch.matmul`](https://pytorch.org/docs/stable/generated/torch.matmul.html) does.\n",
        "\n",
        "Broadcasting can let us easily implement many different operations. For example we can compute an outer product of vectors:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "_W-k7-hpCwlT"
      },
      "outputs": [],
      "source": [
        "# Compute outer product of vectors\n",
        "v = torch.tensor([1, 2, 3])  # v has shape (3,)\n",
        "w = torch.tensor([4, 5])     # w has shape (2,)\n",
        "# To compute an outer product, we first reshape v to be a column\n",
        "# vector of shape (3, 1); we can then broadcast it against w to yield\n",
        "# an output of shape (3, 2), which is the outer product of v and w:\n",
        "print(v.view(3, 1) * w)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "6a9EcX20moP_"
      },
      "source": [
        "We can add a vector to each row of a matrix:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "9bhmBiwcDF1B"
      },
      "outputs": [],
      "source": [
        "x = torch.tensor([[1, 2, 3], [4, 5, 6]])  # x has shape (2, 3)\n",
        "v = torch.tensor([1, 2, 3])               # v has shape (3,)\n",
        "print('Here is the matrix:')\n",
        "print(x)\n",
        "print('\\nHere is the vector:')\n",
        "print(v)\n",
        "\n",
        "# x has shape (2, 3) and v has shape (3,) so they broadcast to (2, 3),\n",
        "# giving the following matrix:\n",
        "print('\\nAdd the vector to each row of the matrix:')\n",
        "print(x + v)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "jYloJIvmm_Me"
      },
      "source": [
        "We can add a vector to each column of a matrix:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "TDTFKACqDK22"
      },
      "outputs": [],
      "source": [
        "x = torch.tensor([[1, 2, 3], [4, 5, 6]])  # x has shape (2, 3)\n",
        "w = torch.tensor([4, 5])                  # w has shape (2,)\n",
        "print('Here is the matrix:')\n",
        "print(x)\n",
        "print('\\nHere is the vector:')\n",
        "print(w)\n",
        "\n",
        "# x has shape (2, 3) and w has shape (2,). We reshape w to (2, 1);\n",
        "# then when we add the two the result broadcasts to (2, 3):\n",
        "print('\\nAdd the vector to each column of the matrix:')\n",
        "print(x + w.view(-1, 1))\n",
        "\n",
        "# Another solution is the following:\n",
        "# 1. Transpose x so it has shape (3, 2)\n",
        "# 2. Since w has shape (2,), adding will broadcast to (3, 2)\n",
        "# 3. Transpose the result, resulting in a shape (2, 3)\n",
        "print((x.t() + w).t())"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "9717YmBBpBfr"
      },
      "source": [
        "Multiply a tensor by a set of constants:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "4UjWDp_XDc_-"
      },
      "outputs": [],
      "source": [
        "x = torch.tensor([[1, 2, 3], [4, 5, 6]])  # x has shape (2, 3)\n",
        "c = torch.tensor([1, 10, 11, 100])        # c has shape (4)\n",
        "print('Here is the matrix:')\n",
        "print(x)\n",
        "print('\\nHere is the vector:')\n",
        "print(c)\n",
        "\n",
        "# We do the following:\n",
        "# 1. Reshape c from (4,) to (4, 1, 1)\n",
        "# 2. x has shape (2, 3). Since they have different ranks, when we multiply the\n",
        "#    two, x behaves as if its shape were (1, 2, 3)\n",
        "# 3. The result of the broadcast multiplication between tensor of shape\n",
        "#    (4, 1, 1) and (1, 2, 3) has shape (4, 2, 3)\n",
        "# 4. The result y has shape (4, 2, 3), and y[i] (shape (2, 3)) is equal to\n",
        "#    c[i] * x\n",
        "y = c.view(-1, 1, 1) * x\n",
        "print('\\nMultiply x by a set of constants:')\n",
        "print(y)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "J2EHXFBFq1ea"
      },
      "source": [
        "**Your turn**: In the file `pytorch101.py`, implement the function `normalize_columns` that normalizes the columns of a matrix. It should compute the mean and standard deviation of each column, then subtract the mean and divide by the standard deviation for each element in the column.\n",
        "\n",
        "Example:\n",
        "```\n",
        "x = [[ 0,  30,  600],\n",
        "     [ 1,  10,  200],\n",
        "     [-1,  20,  400]]\n",
        "```\n",
        "- The first column has mean 0 and std 1\n",
        "- The second column has mean 20 and std 10\n",
        "- The third column has mean 400 and std 200\n",
        "\n",
        "After normalizing the columns, the result should be:\n",
        "```\n",
        "y = [[ 0,  1,  1],\n",
        "     [ 1, -1, -1],\n",
        "     [-1,  0,  0]]\n",
        "```\n",
        "\n",
        "Recall that given scalars $x_1,\\ldots,x_M$ the mean $\\mu$ and standard deviation $\\sigma$ are given by\n",
        "\n",
        "$$\\mu=\\frac{1}{M}\\sum_{i=1}^M x_i \\hspace{4pc} \\sigma = \\sqrt{\\frac{1}{M-1}\\sum_{i=1}^M(x_i-\\mu)^2}$$"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "rVh1DMqMr3zl"
      },
      "outputs": [],
      "source": [
        "from pytorch101 import normalize_columns\n",
        "\n",
        "x = torch.tensor([[0., 30., 600.], [1., 10., 200.], [-1., 20., 400.]])\n",
        "y = normalize_columns(x)\n",
        "print('Here is x:')\n",
        "print(x)\n",
        "print('Here is y:')\n",
        "print(y)\n",
        "\n",
        "x_expected = [[0., 30., 600.], [1., 10., 200.], [-1., 20., 400.]]\n",
        "y_expected = [[0., 1., 1.], [1., -1., -1.], [-1., 0., 0.]]\n",
        "y_correct = y.tolist() == y_expected\n",
        "x_correct = x.tolist() == x_expected\n",
        "print('y correct: ', y_correct)\n",
        "print('x unchanged: ', x_correct)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "NlJs-yN4VTRp"
      },
      "source": [
        "### Out-of-place vs in-place operators\n",
        "Most PyTorch operators are classified into one of two categories:\n",
        "- **Out-of-place operators:** return a new tensor. Most PyTorch operators behave this way.\n",
        "- **In-place operators:** modify and return the input tensor. Instance methods that end with an underscore (such as `add_()` are in-place. Operators in the `torch` namespace can be made in-place using the `out=` keyword argument.\n",
        "\n",
        "For example:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "lnwGzmU9VTRp"
      },
      "outputs": [],
      "source": [
        "# Out-of-place addition creates and returns a new tensor without modifying the inputs:\n",
        "x = torch.tensor([1, 2, 3])\n",
        "y = torch.tensor([3, 4, 5])\n",
        "print('Out-of-place addition:')\n",
        "print('Before addition:')\n",
        "print('x: ', x)\n",
        "print('y: ', y)\n",
        "z = x.add(y)  # Same as z = x + y or z = torch.add(x, y)\n",
        "print('\\nAfter addition (x and y unchanged):')\n",
        "print('x: ', x)\n",
        "print('y: ', y)\n",
        "print('z: ', z)\n",
        "print('z is x: ', z is x)\n",
        "print('z is y: ', z is y)\n",
        "\n",
        "# In-place addition modifies the input tensor:\n",
        "print('\\n\\nIn-place Addition:')\n",
        "print('Before addition:')\n",
        "print('x: ', x)\n",
        "print('y: ', y)\n",
        "x.add_(y)  # Same as x += y or torch.add(x, y, out=x)\n",
        "print('\\nAfter addition (x is modified):')\n",
        "print('x: ', x)\n",
        "print('y: ', y)\n",
        "print('z: ', z)\n",
        "print('z is x: ', z is x)\n",
        "print('z is y: ', z is y)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "uNTk5heeVTRr"
      },
      "source": [
        "In general, **you should avoid in-place operations** since they can cause problems when computing gradients using autograd (which we will cover in a future assignment)."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "uN6FfqU9wFeG"
      },
      "source": [
        "## Running on GPU"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Ds6SDTbrwOc1"
      },
      "source": [
        "**Note: this section requires a GPU! If you do not have a computer with a CUDA-enabled GPU, you can complete this portion of the notebook on Google Colab.**\n",
        "\n",
        "One of the most important features of PyTorch is that it can use graphics processing units (GPUs) to accelerate its tensor operations.\n",
        "\n",
        "We can easily check whether PyTorch is configured to use GPUs:\n",
        "\n",
        "Tensors can be moved onto any device using the .to method."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "_RkoFEVVKWlW"
      },
      "outputs": [],
      "source": [
        "import torch\n",
        "\n",
        "if torch.cuda.is_available():\n",
        "  print('PyTorch can use GPUs!')\n",
        "else:\n",
        "  print('PyTorch cannot use GPUs.')"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "7i_5n_XuKr5k"
      },
      "source": [
        "You can enable GPUs in Colab via Runtime -> Change Runtime Type -> Hardware Accelerator -> GPU.\n",
        "\n",
        "This may cause the Colab runtime to restart, so we will re-import torch in the next cell.\n",
        "\n",
        "We have already seen that PyTorch tensors have a `dtype` attribute specifying their datatype. All PyTorch tensors also have a `device` attribute that specifies the device where the tensor is stored -- either CPU, or CUDA (for NVIDA GPUs). A tensor on a CUDA device will automatically use that device to accelerate all of its operations.\n",
        "\n",
        "Just as with datatypes, we can use the [`.to()`](https://pytorch.org/docs/1.1.0/tensors.html#torch.Tensor.to) method to change the device of a tensor. We can also use the convenience methods `.cuda()` and `.cpu()` methods to move tensors between CPU and GPU."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "D03s614dMCvy"
      },
      "outputs": [],
      "source": [
        "# Construct a tensor on the CPU\n",
        "x0 = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)\n",
        "print('x0 device:', x0.device)\n",
        "\n",
        "# Move it to the GPU using .to()\n",
        "x1 = x0.to('cuda')\n",
        "print('x1 device:', x1.device)\n",
        "\n",
        "# Move it to the GPU using .cuda()\n",
        "x2 = x0.cuda()\n",
        "print('x2 device:', x2.device)\n",
        "\n",
        "# Move it back to the CPU using .to()\n",
        "x3 = x1.to('cpu')\n",
        "print('x3 device:', x3.device)\n",
        "\n",
        "# Move it back to the CPU using .cpu()\n",
        "x4 = x2.cpu()\n",
        "print('x4 device:', x4.device)\n",
        "\n",
        "# We can construct tensors directly on the GPU as well\n",
        "y = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float64, device='cuda')\n",
        "print('y device / dtype:', y.device, y.dtype)\n",
        "\n",
        "# Calling x.to(y) where y is a tensor will return a copy of x with the same\n",
        "# device and dtype as y\n",
        "x5 = x0.to(y)\n",
        "print('x5 device / dtype:', x5.device, x5.dtype)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "O-TDxICdOmJo"
      },
      "source": [
        "Performing large tensor operations on a GPU can be **a lot faster** than running the equivalent operation on CPU.\n",
        "\n",
        "Here we compare the speed of adding two tensors of shape (10000, 10000) on CPU and GPU:\n",
        "\n",
        "(Note that GPU code may run asynchronously with CPU code, so when timing the speed of operations on the GPU it is important to use `torch.cuda.synchronize` to synchronize the CPU and GPU.)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "GW14ZF-_PK7t"
      },
      "outputs": [],
      "source": [
        "import time\n",
        "\n",
        "a_cpu = torch.randn(10000, 10000, dtype=torch.float32)\n",
        "b_cpu = torch.randn(10000, 10000, dtype=torch.float32)\n",
        "\n",
        "a_gpu = a_cpu.cuda()\n",
        "b_gpu = b_cpu.cuda()\n",
        "torch.cuda.synchronize()\n",
        "\n",
        "t0 = time.time()\n",
        "c_cpu = a_cpu + b_cpu\n",
        "t1 = time.time()\n",
        "c_gpu = a_gpu + b_gpu\n",
        "torch.cuda.synchronize()\n",
        "t2 = time.time()\n",
        "\n",
        "# Check that they computed the same thing\n",
        "diff = (c_gpu.cpu() - c_cpu).abs().max().item()\n",
        "print('Max difference between c_gpu and c_cpu:', diff)\n",
        "\n",
        "cpu_time = 1000.0 * (t1 - t0)\n",
        "gpu_time = 1000.0 * (t2 - t1)\n",
        "print('CPU time: %.2f ms' % cpu_time)\n",
        "print('GPU time: %.2f ms' % gpu_time)\n",
        "print('GPU speedup: %.2f x' % (cpu_time / gpu_time))"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "7HEAVPEwviYb"
      },
      "source": [
        "You should see that running the same computation on the GPU was more than 10~30 times faster than on the CPU! Due to the massive speedups that GPUs offer, we will use GPUs to accelerate much of our machine learning code starting in Assignment 2.\n",
        "\n",
        "**Your turn**: Use the GPU to accelerate the following matrix multiplication operation. You should see 5~10x speedup by using the GPU."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "uqEUdst7SAuZ"
      },
      "outputs": [],
      "source": [
        "import time\n",
        "from pytorch101 import mm_on_cpu, mm_on_gpu\n",
        "\n",
        "x = torch.rand(512, 4096)\n",
        "w = torch.rand(4096, 4096)\n",
        "\n",
        "t0 = time.time()\n",
        "y0 = mm_on_cpu(x, w)\n",
        "t1 = time.time()\n",
        "\n",
        "y1 = mm_on_gpu(x, w)\n",
        "torch.cuda.synchronize()\n",
        "t2 = time.time()\n",
        "\n",
        "print('y1 on CPU:', y1.device == torch.device('cpu'))\n",
        "diff = (y0 - y1).abs().max().item()\n",
        "print('Max difference between y0 and y1:', diff)\n",
        "print('Difference within tolerance:', diff < 5e-2)\n",
        "\n",
        "cpu_time = 1000.0 * (t1 - t0)\n",
        "gpu_time = 1000.0 * (t2 - t1)\n",
        "print('CPU time: %.2f ms' % cpu_time)\n",
        "print('GPU time: %.2f ms' % gpu_time)\n",
        "print('GPU speedup: %.2f x' % (cpu_time / gpu_time))"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "vekSz6WtpUXc"
      },
      "source": [
        "Done! Now you can move to kNN.ipynb. Before you move, please check whether you generated any additional cell in every ipynb file (e.g. empty cell after very last code cell)."
      ]
    }
  ],
  "metadata": {
    "accelerator": "GPU",
    "colab": {
      "collapsed_sections": [
        "hQrEwOpXb9Gh",
        "4y93rPhGveWw",
        "oGt8ZPb_vixw",
        "Ad-xqELwyqpN",
        "Ql9_eXuU4OG8",
        "Z150qBob4Wkz",
        "f4SJCVbf-bZ0",
        "WJiiBxNE-X8g",
        "NgcdvD1evxTQ",
        "1BCVlPHZ4_Qz",
        "yDyH9USAuyZ-",
        "lRyLyXU2u29N",
        "mbCVOr2sVTRR",
        "UISn2pcf9QjY",
        "NlJs-yN4VTRp",
        "uN6FfqU9wFeG"
      ],
      "provenance": [],
      "toc_visible": true,
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3 (ipykernel)",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.8.12"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}