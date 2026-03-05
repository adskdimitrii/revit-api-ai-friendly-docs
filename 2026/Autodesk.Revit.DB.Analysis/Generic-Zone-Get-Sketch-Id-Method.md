# Generic Zone Get Sketch Id Method

Source: https://www.revitapidocs.com/2026/abe387d4-22e1-6c40-69a2-d196b14aba58.htm

---

| Generic Zone Get Sketch Id Method |
| --- |

Gets the sketch id for the generic zone. 
**Namespace:** [Autodesk.Revit.DB.Analysis](../ungrouped/Autodesk.-Revit.-DB.-Analysis-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public ElementId GetSketchId()
```

```
Public Function GetSketchId As ElementId
```

```
public:
ElementId^ GetSketchId()
```

```
member GetSketchId : unit -> ElementId 
```

#### Return Value

[ElementId](../Autodesk.Revit.DB/Element-Id-Class.md) 
The sketch element id for the sketch\-based generic zone. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This generic zone must be sketch\-based. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[GenericZone Class](Generic-Zone-Class.md) [Autodesk.Revit.DB.Analysis Namespace](../ungrouped/Autodesk.-Revit.-DB.-Analysis-Namespace.md)
