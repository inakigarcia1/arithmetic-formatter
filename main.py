# This entrypoint file to be used in development. Start by reading README.md
from pytest import main

from arithmetic_arranger import arithmetic_arranger


print(arithmetic_arranger(["1 + 6980", "3801 - 1", "4500 + 4300", "1230 + 4900"], True))


# Run unit tests automatically
main()
