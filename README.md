# i3blocks-blocks

Simple python scripts to be used with the i3bar.

## Requirements

### battery.py 
- Font Awesome
- Python 3
- ACPI

### wifi.py
- Font Awesome
- Python 3
- nmcli

## Example Config:
Add this to your i3blocks.conf
```
[battery]
command=/path/to/script/battery.py
interval=3
```

```
[wifi]
command=/path/to/script/wifi.py
interval=5
```
