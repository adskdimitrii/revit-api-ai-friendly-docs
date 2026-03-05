# Path Reinforcement Alternating Bar Shape Id Property

Source: https://www.revitapidocs.com/2026/192a6b79-2b79-b4f3-a084-8dd0940d9e42.htm

---

| Path Reinforcement Alternating Bar Shape Id Property |
| --- |

The RebarShape element that defines the shape of the alternating bars of the Path Reinforcement. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public ElementId AlternatingBarShapeId { get; set; }
```

```
Public Property AlternatingBarShapeId As ElementId
	Get
	Set
```

```
public:
property ElementId^ AlternatingBarShapeId {
	ElementId^ get ();
	void set (ElementId^ value);
}
```

```
member AlternatingBarShapeId : ElementId with get, set
```

#### Property Value

[ElementId](../Autodesk.Revit.DB/Element-Id-Class.md) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: shapeId should refer to two dimensional Rebar Shape element with segments forming only right angles,  or the Rebar Shape has at least one end treatment or it has at least one crank. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non\-optional argument was null |
| [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | When setting this property: This Path Reinforcement does not have alternating bars enabled.  \-or\-  When setting this property: This PathReinforcement does not host Rebar. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks Changing the value of this property causes the Path Reinforcement to choose values for its
 shape parameters.
 Before calling this method, alternating bars have to be enabled in the Path Reinforcement by setting PATH\_REIN\_ALTERNATING BuiltInParameter. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[PathReinforcement Class](1593a849-b883-73d4-7c02-a2522877d71d.htm) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
