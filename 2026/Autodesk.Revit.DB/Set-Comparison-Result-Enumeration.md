# Set Comparison Result Enumeration

Source: https://www.revitapidocs.com/2026/3310a68d-b67a-79cb-ea54-deb00d9f60d9.htm

---

| Set Comparison Result Enumeration |
| --- |

An enumerated type listing all the relationship types between two sets of arbitrary nature. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public enum SetComparisonResult
```

```
Public Enumeration SetComparisonResult
```

```
public enum class SetComparisonResult
```

```
type SetComparisonResult
```
![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Members 

| Member name | Value | Description |
| --- | --- | --- |
| BothEmpty | 3 | Both sets are empty. |
| Disjoint | 4 | Both sets are not empty and don't overlap. |
| Equal | 64 | Two nonempty sets are equal. |
| LeftEmpty | 1 | The left set is empty and the right set is not. |
| Overlap | 8 | The overlap of two sets is not empty and is a strict subset of both. |
| RightEmpty | 2 | The right set is empty and the left set is not. |
| Subset | 16 | Both sets are not empty and the left set is strict subset of the right. |
| Superset | 32 | Both sets are not empty and the left set is a strict superset of the right. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
