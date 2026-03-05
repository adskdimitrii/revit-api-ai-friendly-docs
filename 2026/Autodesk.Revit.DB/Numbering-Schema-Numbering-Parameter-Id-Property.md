# Numbering Schema Numbering Parameter Id Property

Source: https://www.revitapidocs.com/2026/94659f29-c7f2-9643-f443-9451a3177cc2.htm

---

| Numbering Schema Numbering Parameter Id Property |
| --- |

Id of the parameter that stores values of the numbers on enumerated elements. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public ElementId NumberingParameterId { get; }
```

```
Public ReadOnly Property NumberingParameterId As ElementId
	Get
```

```
public:
property ElementId^ NumberingParameterId {
	ElementId^ get ();
}
```

```
member NumberingParameterId : ElementId with get
```

#### Property Value

[ElementId](Element-Id-Class.md) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks Values of numbers can be obtained by querying this parameter for the respective numbered element. 

*Note: The parameter can be changed directly, but if a value that already exists in the sequence is provided
 a warning will be presented asking the user to select a proper course of action.
 Programmatically with better control the value can be changed(with restrictions) using the [ChangeNumber(String, Int32, Int32\)](Numbering-Schema-Change-Number-Method.md) method.* 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[NumberingSchema Class](Numbering-Schema-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
