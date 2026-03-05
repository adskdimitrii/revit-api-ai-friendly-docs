# Stairs Type Middle Support Type Property

Source: https://www.revitapidocs.com/2026/be91b3a0-047b-bf7f-27e4-3a22c1930735.htm

---

| Stairs Type Middle Support Type Property |
| --- |

The type of middle supports used in the stair. 
**Namespace:** [Autodesk.Revit.DB.Architecture](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public ElementId MiddleSupportType { get; set; }
```

```
Public Property MiddleSupportType As ElementId
	Get
	Set
```

```
public:
property ElementId^ MiddleSupportType {
	ElementId^ get ();
	void set (ElementId^ value);
}
```

```
member MiddleSupportType : ElementId with get, set
```

#### Property Value

[ElementId](../Autodesk.Revit.DB/Element-Id-Class.md) 
invalidElementId if the stairs type has no middle support. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | When setting this property: supportType is not a valid support type. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non\-optional argument was null |
| [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | When setting this property: The stairs type has no middle support so the data being set is not applicable. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[StairsType Class](efa84f53-19fa-039b-c5bb-8fcb72e09878.htm) [Autodesk.Revit.DB.Architecture Namespace](720f0c58-cb2b-4f13-374a-7348ed0a1cd3.htm)
