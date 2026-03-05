# View View Position Id Property

Source: https://www.revitapidocs.com/2026/e6e03c46-d0f6-be1f-f677-a627fb4e742e.htm

---

| View View Position Id Property |
| --- |

The id of the view's saved position. Default is set to ElementId.InvalidElementId. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public ElementId ViewPositionId { get; set; }
```

```
Public Property ViewPositionId As ElementId
	Get
	Set
```

```
public:
property ElementId^ ViewPositionId {
	ElementId^ get ();
	void set (ElementId^ value);
}
```

```
member ViewPositionId : ElementId with get, set
```

#### Property Value

[ElementId](Element-Id-Class.md) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non\-optional argument was null |
| [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | When setting this property: |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[View Class](View-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
