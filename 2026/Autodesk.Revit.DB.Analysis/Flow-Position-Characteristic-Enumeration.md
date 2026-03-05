# Flow Position Characteristic Enumeration

Source: https://www.revitapidocs.com/2026/f42625f2-6e2a-d4dd-aaa8-18de031303c1.htm

---

| Flow Position Characteristic Enumeration |
| --- |

The flow position characteristic of the analytical segment cluster. 
**Namespace:** [Autodesk.Revit.DB.Analysis](../ungrouped/Autodesk.-Revit.-DB.-Analysis-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public enum FlowPositionCharacteristic
```

```
Public Enumeration FlowPositionCharacteristic
```

```
public enum class FlowPositionCharacteristic
```

```
type FlowPositionCharacteristic
```
![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Members 

| Member name | Value | Description |
| --- | --- | --- |
| Branch | 2 | The segment is in the branch direction. |
| Bullhead | 4 | The segment is in the bullhead straight direction where multiple flow paths are combined into the branch segment. |
| BullheadCombined | 5 | The segment is in the bullhead branch direction with combined flow paths. |
| Combined | 3 | The segment flow is combined from multiple other segments. |
| Straight | 1 | The segment is in the straight direction. |
| Undefined | 0 | The flow position characteristic is undefined. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Autodesk.Revit.DB.Analysis Namespace](../ungrouped/Autodesk.-Revit.-DB.-Analysis-Namespace.md)
