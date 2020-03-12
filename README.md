## PlutoX 
Python Api for PlutoX. PlutoX is the Drone from https://www.dronaaviation.com/ 

this is under construction.

### Installation Instruction
```
git clone https://github.com/nittvikas/PlutoX.git
cd PlutoX
pip install -e .
```
---
### Examples
---
###### Note : you must be connected with the PlutoX Wifi.

Arming the Drone and takeoff
```python
from plutox import *
import time

if __name__ == '__main__':
    client = Drone()
    client.arm()
    time.sleep(2)
    client.takeOff()
    time.sleep(2)
    client.land()
    client.disArm()
```
###### Command Functions
| Function Name | Description |
| --- | --- |
| ``` def takeOff()``` | Take of the drone |
| ``` def land()``` | land the Drone, disconnect conection|
| ```frontFlip()``` | flip from front side |
| ```backFlip()``` | flip from back size |
| ```rightFlip()``` | flip from right side |
| ``` leftFlip()``` | flip from right side |
| ``` arm()``` | Arm the drone |
| ``` disArm()``` | Disarm the drone |

##### Note: Work in progress.
