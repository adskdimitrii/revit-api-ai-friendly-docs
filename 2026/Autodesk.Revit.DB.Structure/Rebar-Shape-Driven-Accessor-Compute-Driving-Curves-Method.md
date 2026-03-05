# Rebar Shape Driven Accessor Compute Driving Curves Method

Source: https://www.revitapidocs.com/2026/46288659-93f8-62ee-2d7b-94b7a84e44ab.htm

---

| Rebar Shape Driven Accessor Compute Driving Curves Method |
| --- |

Compute the driving curves. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public IList<Curve> ComputeDrivingCurves()
```

```
Public Function ComputeDrivingCurves As IList(Of Curve)
```

```
public:
IList<Curve^>^ ComputeDrivingCurves()
```

```
member ComputeDrivingCurves : unit -> IList<Curve> 
```

#### Return Value

IList [Curve](../Autodesk.Revit.DB/Curve-Class.md) 
Returns an empty array if an error is encountered. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This RebarShapeDrivenAccessor doesn't contain a valid rebar reference. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks The driving curves are the ones that appear in rebar sketch
 mode. They include lines and arcs that drive the shape, but
 exclude fillets, hooks and cranks. They always lie in a plane\-\-
 if the bar is 3D, these curves are a subset or a projection.
 They are also used for shape matching. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarShapeDrivenAccessor Class](6d2f77e7-bbe2-5bd5-723a-bf27c3df1a65.htm) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
