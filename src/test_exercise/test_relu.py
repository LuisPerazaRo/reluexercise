import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

import pytest
from testbook import testbook

@pytest.fixture(scope='class')
def tb():
    with testbook('../exercise/create_relu.ipynb', execute=['reluclass']) as tb:
        tb.inject("""
torch.manual_seed(42)  # For reproducible tests
""")
        yield tb

def test_positive_relu(tb):
    """
    Test the basic ReLU operation
    """
    # Execute the entire test within the notebook
    result = tb.inject("""
# Test the basic ReLU operation
relu_instance = MyReLU()
test_input = torch.randn((10,10))
relu_output = relu_instance(test_input)
test_passed = (relu_output >= 0).all()
test_passed
""")
    
    assert result, "ReLU should output only non-negative values"

def test_works_as(tb):
    """
    Test if it works as the original Pytorch ReLU
    """
    result = tb.inject("""
# Test if it works as the original PyTorch ReLU
relu_instance = MyReLU()
test_tensor = torch.randn((10,10))
expected = nn.functional.relu(test_tensor)
actual = relu_instance(test_tensor)
test_passed = torch.allclose(expected, actual)
test_passed
""")
    
    assert result, "Custom ReLU does not match PyTorch's ReLU"

def test_inplace(tb):
    """
    Test if the class performs inplace operation
    """
    result = tb.inject("""
# Test if it does inplace operation
relu_instance = MyReLU(inplace=True)
x = torch.randn((10,10))
y = relu_instance(x)
test_passed = id(x) == id(y) and x.data_ptr() == y.data_ptr()
test_passed
""")

    assert result, "The class failed to do ReLU inplace, same memory location"

def test_notinplace(tb):
    """
    Test if the class creates a new object in memory when doing ReLU
    """
    result = tb.inject("""
# Test if it does inplace operation
relu_instance = MyReLU(inplace=False)
x = torch.randn((10,10))
y = relu_instance(x)
test_passed = id(x) != id(y) and x.data_ptr() != y.data_ptr()
test_passed
""")

    assert result, "The class did not created a new tensor in memory"