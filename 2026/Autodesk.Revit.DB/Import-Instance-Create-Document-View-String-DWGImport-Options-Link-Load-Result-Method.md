# Import Instance Create(Document, View, String, DWGImport Options, Link Load Result ) Method

Source: https://www.revitapidocs.com/2026/e0fa547e-65ad-7c72-30c0-2592d181811e.htm

---

| Import Instance Create(Document, View, String, DWGImport Options, Link Load Result ) Method |
| --- |

Creates a new instance of DWG or DXF link type from a file path and loads the linked file. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public static ImportInstance Create(
	Document document,
	View DBView,
	string path,
	DWGImportOptions options,
	out LinkLoadResult linkLoadResult
)
```

```
Public Shared Function Create ( 
	document As Document,
	DBView As View,
	path As String,
	options As DWGImportOptions,
	<OutAttribute> ByRef linkLoadResult As LinkLoadResult
) As ImportInstance
```

```
public:
static ImportInstance^ Create(
	Document^ document, 
	View^ DBView, 
	String^ path, 
	DWGImportOptions^ options, 
	[OutAttribute] LinkLoadResult^% linkLoadResult
)
```

```
static member Create : 
        document : Document * 
        DBView : View * 
        path : string * 
        options : DWGImportOptions * 
        linkLoadResult : LinkLoadResult byref -> ImportInstance 
```

#### Parameters

document [Document](Document-Class.md)
:   The document in which to create the DWG or DXF link.

DBView [View](View-Class.md)
:   The view into which the DWG or DXF link will be created.

path String
:   The full path of the DWG or DXF file to link. The path must exist and must be a valid DWG or DXF file.

options [DWGImportOptions](fcba2c30-7e6d-9ab7-8378-f4c6d5de06bf.htm)
:   Various import options applicable to the DWG format.
 If , all options will be set to their respective default values.

linkLoadResult [LinkLoadResult](f846bfb0-b047-9332-567f-75ae880d8359.htm)
:   An object containing the results of creating and loading
 the DWG or DXF link. It contains the ElementId of the new created DWG or DXF link type.

#### Return Value

[ImportInstance](85b534b8-dd6c-bc13-7c46-c803c83481e4.htm) 
The new instance of DWG or DXF link type. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | document is not a project document.  \-or\-  document is in an edit mode.  \-or\-  Import is temporarily disabled.  \-or\-  The view is not printable.  \-or\-  NullOrEmpty  \-or\-  Not a valid file for DWG import (.dwg and .dxf files are valid).  \-or\-  ThisViewOnly cannot be true when importing a DWG\|DGN drawing into a 3D view.  \-or\-  One or more strings describing layer selection is invalid or empty.  \-or\-  The line weights are not valid; either it contains an invalid number of line weights, or a line weight outside the valid range.  \-or\-  The scale is not valid as a CustomScale for use during import. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [FileArgumentNotFoundException](ca9ccaa9-ed08-d40d-31a7-1af3ad2dcb84.htm) | The given path does not exist. |
| [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Place by shared, and the host model and the link do not share the same coordinate system.  Or place by shared, and the shared coordinates of the host model do not match the GIS coordinate system of the link. |
| [ModificationForbiddenException](53205486-5917-7c33-8e67-e362106ddc97.htm) | The document is in failure mode: an operation has failed,  and Revit requires the user to either cancel the operation  or fix the problem (usually by deleting certain elements).  \-or\-  The document is being loaded, or is in the midst of another  sensitive process. |
| [ModificationOutsideTransactionException](8f025460-c283-ea99-aa8a-5a36e11528f4.htm) | The document has no open transaction. |
| [OptionalFunctionalityNotAvailableException](0612a676-b6ba-8c37-2e28-b197438305ab.htm) | The Material Library is missing in the installed Revit.  \-or\-  The DWG Import/Link module is not available in the installed Revit. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks This function creates a new DWG or DXF link type as well as a new instance of this link type.
 The new instance of DWG or DXF link type is returned by this function and the element id of the new DWG
 or DXF link type is contained in the LinkLoadResult. 

If the given full path of the DWG or DXF file to link is already used by an existing DWG or DXF link type,
 a new instance of this existing DWG or DXF link type will be created and returned. The element id of the existing
 DWG or DXF link type is contained in the LinkLoadResult. 

This function regenerates the input document. 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[ImportInstance Class](85b534b8-dd6c-bc13-7c46-c803c83481e4.htm) [Create Overload](ddb7b91a-482e-5cb6-edf6-913781024602.htm) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
