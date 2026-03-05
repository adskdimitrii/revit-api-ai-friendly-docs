# Rebar Splice By Rules Error Enumeration

Source: https://www.revitapidocs.com/2026/dbb7cba0-7e1c-d8e3-c592-525de1bb571c.htm

---

| Rebar Splice By Rules Error Enumeration |
| --- |

Class that defines states for splicing a Rebar by rules. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public enum RebarSpliceByRulesError
```

```
Public Enumeration RebarSpliceByRulesError
```

```
public enum class RebarSpliceByRulesError
```

```
type RebarSpliceByRulesError
```
![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Members 

| Member name | Value | Description |
| --- | --- | --- |
| CantSpliceAllTheBarsInSet | 7 | Some bars in the varying set are not intersected by the resulting splice geometries. |
| InvalidCombinationOfMaximumMinimumBarLengthAndLapLength | 9 | The combination of the maximum bar length, minimum bar length and lap length is invalid. |
| InvalidRebar | 2 | Free Form rebars, or Shape Driven rebars that are Multiplanar, or have a shape that whose definition is RebarShapeDefinitionByArc, or rebars that are part of a group can't be spliced. |
| LapLengthBiggerThanMaximumBarLength | 8 | The lap length is greater than the maximum length. |
| MaximumLengthBiggerThanBarLength | 5 | The maximum length exceeds the bar length. |
| Success | 0 | Splice by rules can be successfully done. |
| TooBigArc | 6 | The arc segment exceeds the maximum length. |
| TooBigCrank | 10 | The crank lengths exceed the maximum length. |
| TooBigHook | 3 | The hook lengths exceed the maximum length. |
| TooSmallRunOut | 4 | The run\-out is below minimum length, or the lap can't be applied to it. |
| Unknown | 1 | There is an unexpected error. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
