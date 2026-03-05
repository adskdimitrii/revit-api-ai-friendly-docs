# Toposolid Create Sub Division(Document, Element Id, IList Curve Loop ) Method

Source: https://www.revitapidocs.com/2026/6b4bcf67-0432-9549-dafb-464f8ca07eec.htm

---

| Toposolid Create Sub Division(Document, Element Id, IList Curve Loop ) Method |
| --- |

  
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public Toposolid CreateSubDivision(
	Document document,
	ElementId topoTypeId,
	IList<CurveLoop> profiles
)
```

```
Public Function CreateSubDivision ( 
	document As Document,
	topoTypeId As ElementId,
	profiles As IList(Of CurveLoop)
) As Toposolid
```

```
public:
Toposolid^ CreateSubDivision(
	Document^ document, 
	ElementId^ topoTypeId, 
	IList<CurveLoop^>^ profiles
)
```

```
member CreateSubDivision : 
        document : Document * 
        topoTypeId : ElementId * 
        profiles : IList<CurveLoop> -> Toposolid 
```

#### Parameters

document [Document](Document-Class.md)
topoTypeId [ElementId](Element-Id-Class.md)
profiles IList [CurveLoop](84824924-cb89-9e20-de6e-3461f429dfd6.htm)

#### Return Value

[Toposolid](Toposolid-Class.md) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Toposolid Class](Toposolid-Class.md) [CreateSubDivision Overload](Toposolid-Create-Sub-Division-Method.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
