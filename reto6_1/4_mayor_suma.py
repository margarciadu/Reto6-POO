class NotEnoughElementsError(Exception):
    def __init__(self, message="Debe ingresar al menos dos números para calcular la suma de consecutivos."):
        self.message = message
        super().__init__(self.message)

def max_sum_consecutive(nums: list[int]) -> int:
    if len(nums) < 2:
        raise NotEnoughElementsError()
    
    max_sum = nums[0] + nums[1]
    
    for i in range(1, len(nums) - 1):
        current_sum = nums[i] + nums[i + 1]
        if current_sum > max_sum:
            max_sum = current_sum
        
    return max_sum

if __name__ == "__main__":
    try:
        x = input("Ingrese una lista de números separados por espacios: ").strip()
        if not x:
            raise ValueError("No ingresó ningún valor.")
        
        y = list(map(int, x.split()))
        result = max_sum_consecutive(y)
        print("La suma máxima de números consecutivos es:", result)
    
    except ValueError as error:
        print(f"Error: {error}")
    except NotEnoughElementsError as nee:
        print(f"Error: {nee.message}")